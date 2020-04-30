from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, v_id=-1, v_name='', neighbors=None):
        vertex_id = v_id
        vertex_name = v_name
        nbrs = [] if neighbors is None else neighbors

        vertex = Vertex(vertex_id, vertex_name, nbrs)
        self.vertices[vertex_id] = vertex
        self.num_vertices += 1

    def add_edge(self, vid0, vid1, dist):
        self.vertices[vid0].add_neighbor(self.vertices[vid1], dist)
        self.vertices[vid1].add_neighbor(self.vertices[vid0], dist)

    def print_graph(self):
        for v in self.vertices.values():
            v.print_neighbors()

    ###

    def find_path(self, vid0, vid1):
        visited = {}
        for key in self.vertices.keys():
            visited[key] = False

        path = []
        self.find_path_helper(vid0, vid1, visited, path)

    def find_path_helper(self, v0, v1, visited, path):
        visited[v0] = True
        path.append(v0)
        if v0 == v1:
            print(path)
        else:
            for v in self.vertices[v0].get_neighbors():
                i = v.id
                if not visited[i]:
                    self.find_path_helper(i, v1, visited, path)

        path.pop()
        visited[v0] = False

    ###

    def find_path_length(self, vid0, vid1):
        visited = {}
        for key in self.vertices.keys():
            visited[key] = False

        path = []
        self. find_path_length_helper(vid0, vid1, visited, path, 0)

    def find_path_length_helper(self, v0, v1, visited, path, distance_so_far):
        visited[v0] = True
        path.append(v0)

        if v0 == v1:
            print(f'Route: {path}, Length: {distance_so_far} km')
        else:
            for nbor in self.vertices[v0].neighbor_list:  # bu sefer hem neighbor hem uzakligi almak istiyorum
                v_id = nbor[0].id
                distance = nbor[1]
                if not visited[v_id]:
                    self.find_path_length_helper(v_id, v1, visited, path, distance_so_far + distance)

        path.pop()
        visited[v0] = False

    ###

    def find_paths_bfs(self, vid0, vid1):
        visited = {}
        for key in self.vertices.keys():
            visited[key] = False

        paths_queue = []
        paths_queue.append([vid0])

        while len(paths_queue) > 0:
            path = paths_queue.pop(0)  # Fifo
            last_vertex = path[-1]
            if last_vertex == vid1:
                print(path)
            else:
                if not visited[last_vertex]:
                    for v in self.vertices[last_vertex].get_neighbors():
                        i = v.id
                        new_path = list(path)
                        new_path.append(i)
                        paths_queue.append(new_path)
                    visited[last_vertex] = True


g = Graph()
g.add_vertex(55, 'Samsun')
g.add_vertex(53, 'Rize')
g.add_vertex(25, 'Erzurum')
g.add_vertex(61, 'Trabzon')
g.add_vertex(58, 'Sivas')
g.add_vertex(24, 'Erzincan')
g.add_vertex(6, 'Ankara')
g.add_vertex(34, 'Istanbul')
g.add_vertex(19, 'Corum')
g.add_vertex(1, 'Adana')
g.add_vertex(27, 'Gaziantep')

# print(g.num_vertices)

g.add_edge(6, 34, 600)
g.add_edge(19, 6, 250)
g.add_edge(58, 6, 500)
g.add_edge(58, 24, 350)
g.add_edge(24, 25, 200)
g.add_edge(25, 61, 300)
g.add_edge(61, 53, 100)
g.add_edge(61, 55, 400)
g.add_edge(19, 55, 150)

# g.print_graph()
g.find_paths_bfs(34, 25)
