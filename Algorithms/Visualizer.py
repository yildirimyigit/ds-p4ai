import tkinter as tk

from Mazes import WALL, PATH


class MazeApplication(tk.Frame):

    def __init__(self, maze, size=20, user_enabled=False):
        tk.Frame.__init__(self)
        self.maze = maze
        self.rect_ids = [[0] * len(r) for r in maze.maze]

        self.width = len(maze.maze[0])
        self.height = len(maze.maze)
        self.size = size

        self.steps = 0
        self.user_enabled = user_enabled
        self.grid()

        self.top_label = None
        self.canvas = None
        self.bottom_label = None

        self.create_widgets('User' if user_enabled else maze.win_condition)
        self.draw_maze()

        if user_enabled:
            self.create_events()

    def create_widgets(self, win_condition):
        width = self.width * self.size
        height = self.height * self.size

        # Status text is shown
        if self.top_label is None:
            self.top_label = tk.Label(self)
            self.top_label.grid()
        self.top_label.config(text=f'{win_condition}')

        # Where the cells are held
        if self.canvas is None:
            self.canvas = tk.Canvas(self, width=width, height=height)
            self.canvas.grid()

        # Status text is shown
        if self.bottom_label is None:
            self.bottom_label = tk.Label(self)
            self.bottom_label.grid()

    def draw_maze(self):
        for i, row in enumerate(self.rect_ids):
            for j, col in enumerate(row):
                # Calculate start and end points of each cell
                x0, y0 = j * self.size,  i * self.size
                x1, y1 = x0 + self.size, y0 + self.size
                # Get the color of the current cell
                color = self.get_color(x=j, y=i)
                self[i, j] = self.canvas.create_rectangle(x0, y0, x1, y1, width=0, fill=color)

                if self.maze.start_node.x == j and self.maze.start_node.y == i:
                    self.cell = self[j, i]

        self.canvas.tag_raise(self.cell)  # bring to front
        heuristic = self.maze.heuristic.__name__ if self.maze.heuristic else 'Unknown'
        self.bottom_label.config(text=f'Heuristic: {heuristic}\nExpanded: {self.maze.expanded}')

    def create_events(self):
        self.canvas.bind_all('<KeyPress-Up>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Down>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Left>', self.move_cell)
        self.canvas.bind_all('<KeyPress-Right>', self.move_cell)

    def expand(self, node):
        # Draw expansion
        col = self.get_color(node.x, node.y)
        self.canvas.itemconfig(self[node.y, node.x], fill=col if col != 'white' else '#aaa')
        self.canvas.update()

        # Update expanded
        self.bottom_label.config(text=f'Heuristic: {self.maze.heuristic.__name__}\nExpanded: {self.maze.expanded}')

    def move_cell(self, event):
        if event.keysym == 'Up':
            if self.check_move(0, -1):
                self.canvas.move(self.cell, 0, -self.size)
                self.steps += 1
        if event.keysym == 'Down':
            if self.check_move(0, 1):
                self.canvas.move(self.cell, 0, self.size)
                self.steps += 1
        if event.keysym == 'Left':
            if self.check_move(-1, 0):
                self.canvas.move(self.cell, -self.size, 0)
                self.steps += 1
        if event.keysym == 'Right':
            if self.check_move(1, 0):
                self.canvas.move(self.cell, self.size, 0)
                self.steps += 1

        self.bottom_label.config(text=f'Move Count: {self.steps}')
        self.check_status()

    def check_move(self, diff_x, diff_y):
        x0, y0 = self.get_cell_coords()
        x1 = x0 + diff_x
        y1 = y0 + diff_y
        return self.maze.maze[y1][x1] == PATH

    def get_cell_coords(self):
        position = self.canvas.coords(self.cell)
        return position[0] // self.size, position[1] // self.size

    def check_status(self):
        if self.maze.target_node == self.get_cell_coords():
            self.bottom_label.config(text=f'Total move count: {self.steps}')

    def __getitem__(self, item):
        return self.rect_ids[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.rect_ids[key[0]][key[1]] = value

    def get_color(self, x, y):
        if self.maze.start_node.x == x and self.maze.start_node.y == y:
            return 'red'
        elif self.maze.win_condition == 'reach_target' and self.maze.target_node.x == x and self.maze.target_node.y == y:
            return 'green'
        elif self.maze.win_condition == 'eat_all_food' and (x, y) in [n.get_position() for n in self.maze.foods]:
            return 'blue'
        elif self.maze[y, x] == WALL:
            return 'black'
        elif self.maze[y, x] == PATH:
            return 'white'
        else:
            return None
