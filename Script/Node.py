class Graph:
    def __init__(self):
        self.dict = {}

    def addNode(self, node):
        self.dict[node] = []

    def addArc(self, node, node2):
        self.dict[node] = self.dict[node].append(node2)
        self.dict[node2] = self.dict[node2].append(node)
        print(self.dict[node])

    def countNodes(self):
        count = 0
        for i in self.dict:
            count = count + 1
        print(count)

    def countArcs(self):
        count = 0
        for i in self.dict:
            count = count + len(self.dict[i])
        print('numero di archi', count)


xD = []
print('finto: ', len(xD))
myGraph = Graph()
myGraph.addNode(1)
myGraph.addNode(2)
myGraph.addNode(3)
myGraph.addArc(1, 3)

