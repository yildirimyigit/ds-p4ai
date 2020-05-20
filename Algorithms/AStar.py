# Adapted from https://www.annytab.com/a-star-search-algorithm-in-python/
# Example Visualization
# Old project on search algorithms Berkeley http://ai.berkeley.edu/search.html
import copy
import os
import time

from Mazes import *
from Visualizer import MazeApplication


def manhattan(node, other):
    return abs(node.x - other.x) + abs(node.y - other.y)


def diagonal(node, other):
    return max(abs(node.x - other.x), abs(node.y - other.y))


def euclidean(node, other):
    return (abs(node.x - other.x) ** 2 + abs(node.y - other.y) ** 2) ** (1 / 2)


# 1. Problem: Kendi verdiğiniz isme sahip, heuristic fonksyonunuzu yazmaya çalışın!
def my_heuristic(node, other):
    pass


class Maze:
    def __init__(self, win_condition='reach_target', app=None):
        self.start_node = None
        self.target_node = None

        self.row_len = 0
        self.maze = None

        self.expanded = 0
        self.food_count = 0
        self.foods = []
        self.heuristic = None
        self.win_condition = win_condition

        self.app = app
        self.traversal = None

        self.sleep = 0.01

    def set_maze(self, maze_string):
        flatten_maze = maze_string.replace('\n', '')
        s_loc, t_loc = flatten_maze.index(START), flatten_maze.index(TARGET)
        self.row_len = maze_string.index('\n')

        def getxy(loc):
            return loc % self.row_len, loc // self.row_len

        self.start_node = Node(*getxy(s_loc), None)

        if self.win_condition == 'eat_all_food':
            self.food_count = maze_string.count(FOOD)
            self.foods = [Node(*getxy(i), None) for i, c in enumerate(flatten_maze) if c == FOOD]
        elif self.win_condition == 'reach_target':
            self.target_node = Node(*getxy(t_loc), None)

        r_set = [START, TARGET] + ([] if self.win_condition == 'eat_all_food' else [FOOD])
        self.maze = [[PATH if s in r_set else s for s in r] for r in maze_string.split('\n')]

        if self.app:
            self.app = MazeApplication(self)
            self.app.master.title('Maze game')
            self.app.update()
        else:
            self.traversal = copy.deepcopy(self.maze)

        return self

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic
        return self

    def possible_moves(self, node):
        return [(x, y, 1) for x, y in [
            (node.x - 1, node.y),
            (node.x + 1, node.y),
            (node.x, node.y - 1),
            (node.x, node.y + 1)
        ] if self[y, x] != WALL]

    def apply_heuristic(self, node):
        expected_cost = 0
        if self.win_condition == 'reach_target':
            expected_cost = self.heuristic(node, self.target_node)
        elif self.win_condition == 'eat_all_food':
            # Bütün yemekleri ye probleminde bu yaklaşım, şu anki bulunulan noktadan
            # yenmemiş bütün yemeklere olan uzaklıkların toplamını hesaplamak üzerine kurulu.
            #
            # 2. Problem: Bunun yerine yenmemiş en yakın yemekten, ona en yakın yemeğe ve sonrasına
            # en yakın yemeğe gidecek bir yaklaşım score'unuzu geliştirebilir.

            # Yenmemiş tüm yemeklere olan uzaklıklar
            dists = sorted([self.heuristic(node, f) for f in self.foods if (f.x, f.y) not in node.foods])
            # Hesaplanan uzaklıkların toplamı
            expected_cost = 0 if len(dists) == 0 else sum(dists)

        # Heuristic fonksyonunuz 0'dan büyük değer(mantıklı değerler) vermek zorundadır!
        if expected_cost < 0:
            raise Exception(f'Heuristic must be bigger than 0!')
        # [Non-trivial] Başlangıç ve bitiş noktaları haricinde hesaplanan uzaklık 0'dan farklı olmak zorundadır
        elif expected_cost == 0 and len(node.foods) != len(self.foods):
            raise Exception(f'Non-trivial heuristic must be used!')
        # [Admissible] Hesaplanan tahmini uzaklık, gerçek minimum uzaklıktan daha düşük olmak zorundadır.
        #
        # Örneğin midi_corner problemi için en düşük gerçek yol 106 olarak verilmiştir, 106'dan daha büyük
        # değerler hesaplamak hataya sebebiyet verecektir.
        elif expected_cost > 106:
            raise Exception(f'Inadmissible heuristic! {expected_cost}')

        return expected_cost

    def copy(self):
        c_maze = Maze()
        c_maze.start_node = self.start_node
        c_maze.target_node = self.target_node
        c_maze.row_len = self.row_len
        c_maze.maze = copy.deepcopy(self.maze)

        c_maze.expanded = self.expanded
        c_maze.heuristic = self.heuristic
        c_maze.food_count = self.food_count
        c_maze.foods = self.foods
        c_maze.win_condition = self.win_condition
        return c_maze

    def has_completed(self, current_node):
        if self.win_condition == 'reach_target':
            return current_node == self.target_node
        elif self.win_condition == 'eat_all_food':
            return len(current_node.foods) == self.food_count

    def update(self, node):
        if self.win_condition == 'reach_target':
            self[node.y, node.x] = f'{node.g%10}'
        elif self[node.y, node.x] not in '0123456789' or int(self[node.y, node.x]) < len(node.foods):
            self[node.y, node.x] = f'{len(node.foods)}'

    def viz_update(self, node):
        if self.app:
            self.app.expand(node)
        else:
            if self.win_condition == 'reach_target':
                self.traversal[node.y][node.x] = f'{node.g%10}'
            elif self.traversal[node.y][node.x] not in '0123456789' or \
                    int(self.traversal[node.y][node.x]) < len(node.foods):
                self.traversal[node.y][node.x] = f'{len(node.foods)}'

            self.pprint()

        time.sleep(self.sleep)

    def clear_stats(self):
        if self.app:
            self.app.draw_maze()
        else:
            self.traversal = copy.deepcopy(self.maze)
        self.expanded = 0

    def pprint(self, search_state=True):
        os.system('clear')
        print(self.win_condition)
        print(Maze.maze2str(self.traversal) if search_state else self)
        print(f'Heuristic: {self.heuristic.__name__}\nExpanded: {self.expanded}')

    def get_path(self, node):
        if self.app:
            self.app.draw_maze()
        else:
            self.traversal = copy.deepcopy(self.maze)
        path = []
        while node != maze.start_node:
            # [Consistent] seçilen hareket sonucu varılan noktada hesaplanan tahmini uzaklık
            # şu anda hesaplanan tahmini uzaklık farkı, o hareketi yapmak için gereken harcamadan
            # büyük olmak zorundadır.
            #
            # Bir hareketin maliyeti: 1
            # t zamanında hesaplanan h: 16
            # t+1 zamanında hesaplanan h - 16 > 1
            if node.parent != maze.start_node and node.h - node.parent.h > 1:  # Step cost is 1
                raise Exception(f'Inconsistent heuristic! {node.parent.h} -> {node.h}')

            # Print current status
            self.viz_update(node)

            # Add to path and move to parent
            path.append(node)
            node = node.parent

        # Add start
        path.append(node)

        # Print current status
        self.viz_update(node)

        return path[::-1]

    @staticmethod
    def maze2str(maze):
        return f'  {"".join([str(i%10) for i in range(len(maze[0]))])}\n' + \
               '\n'.join([f'{i%10} ' + ''.join([s for s in r]) for i, r in enumerate(maze)])

    def __getitem__(self, item):
        return self.maze[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.maze[key[0]][key[1]] = value

    def __str__(self):
        return Maze.maze2str(self.maze)


# This class represents a node
class Node:

    # Initialize the class
    def __init__(self, x, y, parent, foods=None):
        self.x = x
        self.y = y

        self.parent = parent
        self.foods = [] if foods is None else sorted(set(foods))

        self.g = 0  # Distance to start node
        self.h = 0  # Expected Distance to goal node
        self.f = 0  # Total cost

    def neighbors(self, maze):
        return [(Node(x, y, self, self.foods + ([(x, y)] if maze[y, x] == FOOD else [])), c)
                for x, y, c in maze.possible_moves(self)]

    def get_position(self):
        return self.x, self.y

    def estimate(self, maze, cost):
        # Generate heuristics (Manhattan distance)
        self.g = self.parent.g + cost
        self.h = maze.apply_heuristic(self)
        self.f = self.g + self.h

    # Compare nodes
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.foods == other.foods

    # Sort nodes
    def __lt__(self, other):
        # 3. Problemin çözümünde burası ile oynayarak open_list içerisindeki
        # sıralamanın değişmesini sağlayabilir ve bunun score'a etkisini
        # inceleyebilirsiniz.
        # Mesela "Bütün yemekleri ye" problemi için bir yemi yediğiniz durumları
        # öncelikli değerlendirmek (f değerinden önce) score'unuzu geliştirebilir.
        return self.f < other.f

    # Print node
    def __repr__(self):
        return f'(({self.x}, {self.y}),{self.f},{self.foods})'


# Check if a neighbor should be added to open list
def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


def astar_search(maze, app=None):
    # Create lists for open nodes and closed nodes
    open_list = [maze.start_node]
    closed_list = []

    # Loop until the open list is empty
    while len(open_list) > 0:
        # input()
        # Sort the open list to get the node with the lowest cost first
        open_list.sort()

        # Get the node with the lowest cost
        current_node = open_list.pop(0)

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Print current status
        maze.viz_update(current_node)
        if app:
            app.expand(current_node)

        # Check if we have reached the goal, return the path
        if maze.has_completed(current_node):
            return maze.get_path(current_node)

        # Loop neighbors
        for neighbor, cost in current_node.neighbors(maze):
            maze.expanded += 1

            # Check if the neighbor is in the closed list
            if neighbor in closed_list:
                continue

            # Generate heuristics (Manhattan distance)
            neighbor.estimate(maze, cost)

            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open_list, neighbor):
                # Everything is green, add neighbor to open list
                open_list.append(neighbor)

    # Return None, no path is found
    return None


if __name__ == "__main__":
    # Hedefe gitme problemi, ikinci parametre True olduğunda
    # videodaki görselleştirme çalışacaktır. (Bunun olması için tkinter
    # kütüphanesini kurmuş olmanız gerekiyor)

    # midi_corner labirenti için tasarlandı ama Mazes.py içerisindeki
    # diğer haritaları da deneyebilirsiniz (.set_maze(tiny_corner))
    maze = Maze('reach_target', False).set_maze(midi_corner)

    # .set_heuristic(my_heuristic) şeklinde çalıştırarak kendi kodunuzu
    # test edebilirsiniz!
    astar_search(maze.set_heuristic(manhattan))
    # Aynı maze'i başka heuristic'ler ile denemek isterseniz,
    # her seferinde değerleri 0'lamanız gerekiyor.
    maze.clear_stats()
    astar_search(maze.set_heuristic(diagonal))
    maze.clear_stats()
    astar_search(maze.set_heuristic(euclidean))
    maze.clear_stats()

    # Bütün yemekleri yeme problemi
    maze = Maze('eat_all_food', False).set_maze(midi_corner)

    astar_search(maze.set_heuristic(manhattan))
    maze.clear_stats()
    # Consistant olmayan fonksyonlar!
    astar_search(maze.set_heuristic(diagonal))
    maze.clear_stats()
    astar_search(maze.set_heuristic(euclidean))
    maze.clear_stats()

    # 1. 'reach_target', Kendi heuristic'inizi yazın ve deneyin. (Kodun en üstünde)
    # 2. 'eat_all_food', Score'u geliştirmeye çalışın.
    # (yemekler arası mesafe denenebilir, Maze.apply_heuristic fonksyonunu inceleyin.)
    # 3. 'eat_all_food', Score'u geliştirmeye çalışın.
    # (Node/State'lerin öncelik sıralamasına yenilen yemek sayısını entegre etmeyi deneyebilirsiniz.
    # Node.__lt__() fonksyonunu inceleyin.)
