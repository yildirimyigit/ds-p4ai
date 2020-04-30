class Vertex:
    def __init__(self, v_id=-1, v_name='', v_nbors=None):
        self.id = v_id
        self.name = v_name
        if v_nbors is None:
            self.neighbor_list = []  # list of tuples in form (vertex, distance)
        else:
            self.neighbor_list = v_nbors

    def add_neighbor(self, vertex, distance):
        self.neighbor_list.append((vertex, distance))

    def get_neighbors(self):
        nbors = []
        for vertex, d in self.neighbor_list:
            if vertex in nbors:
                pass
            else:
                nbors.append(vertex)
        return nbors

    def print_neighbors(self):
        print(f'{self.name}({self.id}):')
        nbors = self.get_neighbors()
        for i, n in enumerate(nbors):
            print(f'  -{i+1}: {n.name}')

#
# v0 = Vertex(6, 'Ankara')
# v1 = Vertex(34, 'Istanbul')
# v2 = Vertex(19, 'Corum')
#
# v0.add_neighbor(v1, 600)
# v0.add_neighbor(v2, 250)
#
# v0.print_neighbors()
# v1.print_neighbors()
