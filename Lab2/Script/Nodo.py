
class Node:
    def __init__(self, nome, lng, lat):
        self.nome = nome
        self.lng = lng
        self.lat = lat
        self.adj = set()

    def addAdj(self, node):
        self.adj.add(node)

class Edge:
    def __init__(self):
        self.times = set()

    # d_time: departure time
    # a_time: arrival time
    def addTimes(self, d_time, a_time):
        self.times.add((d_time, a_time))


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def addNode(self, id, nome, lng, lat):
        if id not in self.nodes:
            self.nodes[id] = Node(nome, lng, lat)

    def addEdgeTimes(self, nodo1, nodo2, id, d_time, a_time):
        if (nodo1, nodo2, id) not in self.edges:
            self.edges[(nodo1, nodo2, id)] = Edge()
            self.nodes[nodo1].addAdj(nodo2)

        self.edges[(nodo1, nodo2, id)].addTimes(d_time, a_time)



