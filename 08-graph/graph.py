from queue import PriorityQueue

class Graph:
    def __init__(self) -> None:
        self.vertices = {}
        self.directed = False 
        self.path = ''

    def add_vertex(self, id, data=None):
        if id in self.vertices:
            print("Vertex already in graph")
        else: 
            vertex = Vertex(id)
            self.vertices[id] = vertex

    def add_edge(self, ida, idb, weight=1):
        if ida in self.vertices and idb in self.vertices:
            edge = Edge(idb, weight)
            self.vertices[ida].add_edge(idb, edge)
            if not self.directed:
                edge = Edge(ida, weight)
                self.vertices[idb].add_edge(ida, edge)

    def display(self):
        for v in self.vertices:
            print(v, "(", self.vertices[v].distance, ")", end='. ')
            print('Edges: ', end='')
            for e in self.vertices[v].edges:
                edge = self.vertices[v].edges[e]
                print('[', e, edge.weight, '] ', end='')
            print()

    def bfs(self, start):
        if start not in self.vertices:
            print("Starting vertex not found")
            return
        for v in self.vertices:
            self.vertices[v].init_bfs()
        queue = []
        queue.append(self.vertices[start])
        self.vertices[start].color = 'gray'
        self.vertices[start].distance = 0
        while len(queue) > 0:
            vertex = queue.pop(0)
            for e in vertex.edges:
                did = vertex.edges[e].destination
                destination = self.vertices[did]
                if destination.color == 'white':
                    destination.color = 'gray'
                    destination.parent = vertex
                    destination.distance = vertex.distance + 1
                    queue.append(destination)
            vertex.color = 'black'

    def print_shortest_path(self, start, dest):
        start_vertex = self.vertices[start]
        dest_vertex = self.vertices[dest]
        if dest_vertex.parent is not None:
            self.print_shortest_path(start, dest_vertex.parent.id)
        elif dest != start:
            self.path = "No path from start to dest"
            return
        self.path += str(dest) + ' ' 

    def relax(self, va, vb, w):
        if vb.distance > va.distance + w:
            vb.distance = va.distance + w
            vb.parent = va

    def dijkstra(self, start):
        for v in self.vertices:
            self.vertices[v].init_bfs()
        self.vertices[start].distance = 0
        Q = []
        for vertex in self.vertices:
            Q.append(self.vertices[vertex])
        Q.sort(key=lambda x : x.distance)
        while(len(Q) > 0):
            u = Q.pop(0)
            for edge in u.edges:
                v = self.vertices[edge]
                w = u.edges[edge].weight
                self.relax(u, v, w)
            Q.sort(key=lambda x : x.distance)




class Vertex:
    def __init__(self, id) -> None:
        self.id = id
        self.edges = {}
        # These variables below used for BFS and Dijkstra
        self.distance = 0
        self.color = 'white'
        self.parent = None

    def add_edge(self, idb, edge):
        self.edges[idb] = edge

    def init_bfs(self):
        self.distance = float('inf')
        self.color = 'white'
        self.parent = None


class Edge:
    def __init__(self, destination, weight=1) -> None:
        self.destination = destination
        self.weight = weight


if __name__ == "__main__":
    g = Graph()
    g.directed = True
    vertices = ['A','B','C','D','G','F','H','J','K', 'X']
    for v in vertices:
        g.add_vertex(v)
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 5)
    g.add_edge('B', 'D', 4)
    g.add_edge('B', 'G', 7)
    g.add_edge('C', 'F', 1)
    g.add_edge('G', 'H', 3)
    g.add_edge('G', 'F', 4)
    g.add_edge('F', 'H', 2)
    g.add_edge('F', 'J', 6)
    g.add_edge('H', 'D', 3)
    g.add_edge('H', 'J', 5)
    g.add_edge('D', 'K', 6)
    g.add_edge('D', 'J', 2)
    g.add_edge('D', 'H', 2)
    g.add_edge('J', 'K', 2)
    # g.display()
    g.dijkstra('A')
    # g.display()
    g.print_shortest_path('A', 'X')
    print(g.path)


# if __name__ == '__main__':
#     g = Graph()
#     g.add_vertex('a')
#     g.add_vertex('b')
#     g.add_vertex('c')
#     g.add_vertex('d')
#     g.add_vertex('e')
#     g.add_vertex('f')
#     g.add_vertex('g')
#     g.add_vertex('h')
#     g.add_vertex('i')
#     g.add_edge('a', 'b')
#     g.add_edge('a', 'e')
#     g.add_edge('a', 'd')
#     g.add_edge('a', 'f')
#     g.add_edge('b', 'g')
#     g.add_edge('b', 'c')
#     g.add_edge('b', 'e')
#     g.add_edge('c', 'g')
#     g.add_edge('c', 'e')
#     g.add_edge('d', 'e')
#     g.add_edge('e', 'f')
#     g.add_edge('f', 'g')
#     g.add_edge('h', 'i')
#     g.display()
#     g.bfs('a')
#     g.print_shortest_path('a', 'g')
#     print(g.path)


    # graph1 = Graph()
    # graph1.add_vertex(1)
    # graph1.add_vertex(2)
    # graph1.add_vertex(3)
    # graph1.add_vertex(4)
    # graph1.add_vertex(5)
    # graph1.add_edge(1, 2)
    # graph1.add_edge(1, 5)
    # graph1.add_edge(2, 5)
    # graph1.add_edge(2, 4)
    # graph1.add_edge(2, 3)
    # graph1.add_edge(3, 4)
    # graph1.add_edge(4, 5)
    # graph1.display()

    # graph1.bfs(1)
    # graph1.print_shortest_path(1, 3)

    # print()
    # graph2 = Graph()
    # graph2.directed = True
    # for i in range(1, 7):
    #     graph2.add_vertex(i)
    # graph2.add_edge(1, 2)
    # graph2.add_edge(1, 4)
    # graph2.add_edge(2, 5)
    # graph2.add_edge(3, 5)
    # graph2.add_edge(3, 6)
    # graph2.add_edge(4, 2)
    # graph2.add_edge(5, 4)
    # graph2.add_edge(6, 6)
    # graph2.display()
