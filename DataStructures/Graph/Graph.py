# Adopted from: https://www.bogotobogo.com/python/python_graph_data_structures.php
from DataStructures.LinkedLists import Queue, Stack


class Vertex:
    def __init__(self, v_id):
        self.id = v_id
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_neighbors(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, v_id):
        new_vertex = Vertex(v_id)

        self.vertex_dict[v_id] = new_vertex
        self.num_vertices += 1

        return new_vertex

    def get_vertex(self, v_id):
        return self.vertex_dict.get(v_id, None)

    def add_edge(self, v_from, v_to, cost=0, undirected=True):
        if v_from not in self.vertex_dict:
            self.add_vertex(v_from)
        if v_to not in self.vertex_dict:
            self.add_vertex(v_to)

        self.vertex_dict[v_from].add_neighbor(self.vertex_dict[v_to], cost)
        if undirected:
            self.vertex_dict[v_to].add_neighbor(self.vertex_dict[v_from], cost)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def dfs_rec_help(self, start_id, visited):
        visited[start_id] = True
        curr_node = self.vertex_dict[start_id]
        print(f'{curr_node.id}', end=', ')

        for neighbor in curr_node.get_neighbors():
            if not visited[neighbor.id]:
                self.dfs_rec_help(neighbor.id, visited)

    def dfs_rec(self, start_id):
        visited = {k: False for k in self.vertex_dict.keys()}

        self.dfs_rec_help(start_id, visited)

    def dfs(self, start_id):
        pass


if __name__ == '__main__':
    undirected = True
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7, undirected)
    g.add_edge('a', 'c', 9, undirected)
    g.add_edge('a', 'f', 14, undirected)
    g.add_edge('b', 'c', 10, undirected)
    g.add_edge('b', 'd', 15, undirected)
    g.add_edge('c', 'd', 11, undirected)
    g.add_edge('c', 'f', 2, undirected)
    g.add_edge('d', 'e', 6, undirected)
    g.add_edge('e', 'f', 9, undirected)

    for v in g:
        for w in v.get_neighbors():
            print(f'{v.get_id()}, {w.get_id()}, {v.get_weight(w)}')

    for v in g:
        print(f'g.vertex_dict[{v.get_id()}] = {g.vertex_dict[v.get_id()]}')

    g.dfs_rec('a')
    print()
    g.dfs('a')

