from Script import DFS


class Graph:
    def __init__(self,num):
        self.dict = {}
        for i in range(1, num +1):
            self.addNode(i)

    def addNode(self, node):
        if not node in self.dict:
            self.dict[node] = []

    def addArc(self, node, node2):
        if node != node2 and self.dict[node].count(node2) == 0:
            self.dict[node].append(node2)
            self.dict[node2].append(node)

    def countNodes(self):
        count = 0
        for i in self.dict:
            count = count + 1
        return count

    def countArcs(self):
        count = 0
        for i in self.dict:
            count = count + len(self.dict[i])
        return int(count/2)

    def getNodeDegree(self,n):
        return len(self.dict.get(n))

    def getGraphDegree(self):
        max = 0
        for i in self.dict:
            iDegree = len(self.dict.get(i))
            if iDegree > max:
                max = iDegree
        return max

    def getAvarageDegree(self):
        degreeSum = 0
        for v in self.dict:
            degreeSum = degreeSum + self.getNodeDegree(v)
        return degreeSum/self.countNodes()

    def getMaxDegree(self):
        g_max = 0
        for n in self.dict:
            l_max = self.getNodeDegree(n)
            if l_max > g_max:
                g_max = l_max
        return g_max;

    def getMaxDegreeNode(self):
        max_n = -1
        max_g = -1
        for n in self.dict:
            local_max_g = self.getNodeDegree(n)
            if local_max_g > max_g:
                max_g = local_max_g
                max_n = n
        return max_n

    def getNodeAdj(self,n):
        return self.dict.get(n, [])

    def present(self, n):
        return n in self.dict

    def isEmpty(self):
        return not self.dict

    def getNodes(self):
        return self.dict.keys()

    def removeNode(self, n):
        if self.dict.pop(n, False):
            self.removeArcToN(n)

    def removeArcToN(self, n):
        for k in self.dict:
            if n in self.getNodeAdj(k):
                self.dict[k].remove(n)

    def __str__(self):
        return self.dict.__str__()

    def getMaxCC(self):
        CC = DFS.ConnectedC(self)
        max = 0
        for list in CC:
            if len(list) > max:
                max = len(list)
        return max

    def getResilience(self, initialNodeNumber):
        return self.getMaxCC()/initialNodeNumber


