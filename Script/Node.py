class Graph:
    def __init__(self):
        self.dict = {}

    def addNode(self, node):
        self.dict[node] = []

    def addArc(self, node, node2):
        self.dict[node].append(node2)
        self.dict[node2].append(node)

    def countNodes(self):
        count = 0
        for i in self.dict:
            count = count + 1
        print('numero di nodi', count)
        return count

    def countArcs(self):
        count = 0
        for i in self.dict:
            count = count + len(self.dict[i])
        print('numero di archi', count)
        return count


xD = []
xD.append(5)
print('finto: ', len(xD))
myGraph = Graph()
myGraph.addNode(1)
myGraph.addNode(2)
myGraph.addNode(3)
myGraph.addArc(1, 3)
print(myGraph.dict)

