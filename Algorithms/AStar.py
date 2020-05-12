# Adapted from https://www.annytab.com/a-star-search-algorithm-in-python/
# Example Visualization
# Old project on search algorithms Berkeley http://ai.berkeley.edu/search.html
import copy
import os
import time

from Maze import *


# This class represents a node
class Node:

    # Initialize the class
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y

        self.parent = parent

        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    def neighbors(self):
        return [(Node(self.x - 1, self.y, self), 1),
                (Node(self.x + 1, self.y, self), 1),
                (Node(self.x, self.y - 1, self), 1),
                (Node(self.x, self.y + 1, self), 1)]

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def diagonal(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def euclidian(self, other):
        return (abs(self.x - other.x)**2 + abs(self.y - other.y)**2)**(1/2)

    def estimate(self, goal, cost, heuristics='manhattan'):
        # Generate heuristics (Manhattan distance)
        self.g = self.parent.g + cost
        if heuristics == 'manhattan':
            self.h = self.manhattan(goal)
        elif heuristics == 'diagonal':
            self.h = self.diagonal(goal)
        elif heuristics == 'euclidian':
            self.h = self.euclidian(goal)
        self.f = self.g + self.h

    # Compare nodes
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return f'(({self.x}, {self.y}),{self.f})'


# Check if a neighbor should be added to open list
def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


def astar_search(maze, start_node, goal_node, heuristic):
    traversal = copy.deepcopy(maze)
    # Create lists for open nodes and closed nodes
    open_list = [start_node]
    closed_list = []

    # Loop until the open list is empty
    while len(open_list) > 0:

        # Sort the open list to get the node with the lowest cost first
        open_list.sort()

        # Get the node with the lowest cost
        current_node = open_list.pop(0)

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Print current status
        traversal[current_node.y][current_node.x] = f'{current_node.g%10}'
        print_maze(traversal)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            traversal = copy.deepcopy(maze)
            path = []
            while current_node != start_node:
                # Print current status
                traversal[current_node.y][current_node.x] = f'{current_node.g%10}'
                print_maze(traversal)

                # Add to path and move to parent
                path.append(current_node)
                current_node = current_node.parent

            # Add start
            path.append(current_node)

            # Print current status
            traversal[current_node.y][current_node.x] = f'{current_node.g%10}'
            print_maze(traversal)

            return path[::-1]

        # Loop neighbors
        for neighbor, cost in current_node.neighbors():

            # Get value from map
            map_value = maze[neighbor.y][neighbor.x]

            # Check if the node is a wall
            if map_value == WALL:
                continue

            # Check if the neighbor is in the closed list
            if neighbor in closed_list:
                continue

            # Generate heuristics (Manhattan distance)
            neighbor.estimate(goal_node, cost, heuristic)

            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open_list, neighbor):
                # Everything is green, add neighbor to open list
                open_list.append(neighbor)

    # Return None, no path is found
    return None


def print_maze(maze):
    os.system('clear')
    print('\n'.join([''.join([s for s in r]) for r in maze]))
    time.sleep(.1)


if __name__ == "__main__":
    s_loc, t_loc = midi_corner.replace('\n', '').index('S'), midi_corner.replace('\n', '').index('T')
    row_len = midi_corner.index('\n')
    start_node = Node(s_loc % row_len, s_loc // row_len, None)
    goal_node = Node(t_loc % row_len, t_loc // row_len, None)

    maze = [[' ' if s in ['S', 'T'] else s for s in r] for r in midi_corner.split('\n')]
    print_maze(maze)

    astar_search(maze, start_node, goal_node, 'manhattan')
    astar_search(maze, start_node, goal_node, 'diagonal')
    astar_search(maze, start_node, goal_node, 'euclidian')

    # path = astar_search(maze, start_node, goal_node, 'manhattan')
    # print(*path, sep='\n')
