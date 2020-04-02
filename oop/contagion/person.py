"""
  @author: yigit.yildirim@boun.edu.tr
"""
import random


class Person:
    """
    p: position
    g: goal
    """
    def __init__(self, id_in, world, hz, p=(-1, -1), g=(-1, -1), move_by=1.5, lim_goal=5000):
        self.id = id_in
        self.world = world
        self.isolated = False
        self.move_by = move_by
        self.lim_goal = lim_goal
        self.size = 10
        self.radius = self.size / 2
        self.position = p if p != (-1, -1) else self.generate_random_position()
        self.circle = self.world.canvas.create_oval(self.position[0] - self.radius, self.position[1] - self.radius,
                                                    self.position[0] + self.radius, self.position[1] + self.radius,
                                                    fill="#32527B")
        self.update_freq = int(1000/hz)  # no of calls in 1000 ms
        self.dir = (0, 0)
        if g != (-1, -1):
            self.goal = g
        else:
            self.set_goal()

        self.infected = False

    def generate_random_position(self):
        # generating a random position inside the world
        lim_x = self.world.end_point[0]
        lim_y = self.world.end_point[1]
        rand_x = random.randint(self.radius, lim_x-self.radius)
        rand_y = random.randint(self.radius, lim_y-self.radius)
        return rand_x, rand_y

    def set_goal(self, g=(-1, -1)):
        if g == (-1, -1):
            self.goal = self.generate_random_goal()
        else:
            self.goal = g

        self.set_direction()

    def generate_random_goal(self):
        # generating random goals outside the world
        lim_x = self.world.end_point[0]
        lim_y = self.world.end_point[1]

        rand_x, rand_y = 0, 0
        while 0 <= rand_x <= lim_x:
            rand_x = random.randint(-self.lim_goal, self.lim_goal)
        while 0 <= rand_y <= lim_y:
            rand_y = random.randint(-self.lim_goal, self.lim_goal)
        return rand_x, rand_y

    def conflict(self, person):
        # lim_x = self.world.end_point[0]
        # lim_y = self.world.end_point[1]

        if person.infected:
            self.infected = True
            self.world.canvas.itemconfig(self.circle, fill='#808080')

        # if on_left:  # if on left, create new goal on left
        #     new_x = random.randint(-self.lim_goal, 0)
        # else:
        #     new_x = random.randint(lim_x, self.lim_goal)
        #
        # new_y = 0
        # while 0 <= new_y <= lim_y:
        #     new_y = random.randint(-self.lim_goal, self.lim_goal)
        #
        # self.goal = (new_x, new_y)
        self.set_goal()

    def set_direction(self):
        # position and goal are 2D points on XY coordinate system.
        diff_x = self.goal[0] - self.position[0]
        diff_y = self.goal[1] - self.position[1]

        length = (diff_x ** 2 + diff_y ** 2) ** 0.5

        self.dir = (diff_x / length, diff_y / length)

    def move_towards_goal(self):
        delta_x = self.dir[0] * self.move_by
        delta_y = self.dir[1] * self.move_by

        reached_wall = False

        left = self.position[0] - self.radius
        right = self.position[0] + self.radius
        up = self.position[1] - self.radius
        down = self.position[1] + self.radius

        h_side = left if delta_x < 0 else right
        v_side = up if delta_y < 0 else down

        if h_side + delta_x >= self.world.end_point[0] or h_side + delta_x <= 0:
            self.set_goal((-1 * self.goal[0], self.goal[1]))
            reached_wall = True
        if v_side + delta_y >= self.world.end_point[1] or v_side + delta_y <= 0:
            self.set_goal((self.goal[0], -1 * self.goal[1]))
            reached_wall = True
        if not reached_wall:
            self.world.canvas.move(self.circle, delta_x, delta_y)
            self.position = (self.position[0] + delta_x, self.position[1] + delta_y)

        self.world.notify(self.circle)
        self.world.canvas.after(self.update_freq, self.move_towards_goal)
