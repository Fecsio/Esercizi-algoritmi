class Graph:
    def __init__(self,num):
        self.dict = {}
        for i in range(1, num +1):
            self.addNode(i)

    def addNode(self, node):
        self.dict[node] = []

    def addArc(self, node, node2):
        if node != node2 and self.dict[node].count(node2) == 0:
            self.dict[node].append(node2)
            self.dict[node2].append(node)

    def countNodes(self):
        count = 0
        for i in self.dict:
            count = count + 1
        print('numero di nodi:', count)
        return count

    def countArcs(self):
        count = 0
        for i in self.dict:
            count = count + len(self.dict[i])
        print('numero di archi', count)
        return count

    def getNodeDegree(self,n):
        print('grado di n:', len(self.dict.get(n)))
        return len(self.dict.get(n))

    def getGraphDegree(self):
        max = 0
        for i in self.dict:
            iDegree = len(self.dict.get(i))
            if iDegree > max:
                max = iDegree
        print('grado del grafo: ', max)
        return max

    def getAvarageDegree(self):
        return self.getGraphDegree()/self.countNodes()

    def __str__(self):
        return self.dict.__str__()
