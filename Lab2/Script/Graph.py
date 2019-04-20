from Lab2.Script import Time


class Node:
    def __init__(self, nome, lng, lat):
        self.nome = nome
        self.lng = lng
        self.lat = lat
        self.adj = set()

    def addAdj(self, node):
        self.adj.add(node)

    def getLng(self):
        return self.lng

    def getLat(self):
        return self.lat


class Edge:
    def __init__(self, idE, d_time, a_time):
        assert d_time.seconds <= a_time.seconds
        self.times = [d_time, a_time]
        self.id = idE
        self.weight = a_time.seconds - d_time.seconds

    def __str__(self):
        s = "id: " + self.id + " tempi" + str(self.times[0]) + " " + str(self.times[1])
        return s

    def __repr__(self):
        s = "id: " + self.id + " tempi: " + str(self.times[0]) + " " + str(self.times[1])
        return s

    # d_time: departure time
    # a_time: arrival time
    def addTimes(self, idE, d_time, a_time):

        self.times.add((Time.Time(d_time), Time.Time(a_time)))


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def addNode(self, id, nome, lng, lat):
        if id not in self.nodes:
            self.nodes[id] = Node(nome, lng, lat)

    def addEdgeTimes(self, nodo1, nodo2, idE, d_time, a_time):
        if (nodo1, nodo2) not in self.edges:
            self.nodes[nodo1].addAdj(nodo2)
            self.edges[(nodo1, nodo2)] = [Edge(idE, Time.Time(d_time), Time.Time(a_time))]
        else:
            self.edges[(nodo1, nodo2)].append(Edge(idE, Time.Time(d_time), Time.Time(a_time)))


