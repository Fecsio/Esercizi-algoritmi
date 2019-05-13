
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def __ne__(self, other):
        self.value != other.value

class Set:
    def __init__(self):
        self.setList = []

    def makeSet(self, node):
        self.setList.append(Node(node))

    def findSet(self, node):
        parent = self.setList[node].getParent()
        if parent != self.setList[node]:
            parent.setParent(self.findSet(parent.getValue()))
        return parent

    def union(self, node1, node2):
        x = self.findSet(self.setList[node1].getValue())
        y = self.findSet(self.setList[node2].getValue())
        if x.rank > y.rank:
            y.setParent(x)
        else:
            x.setParent(y)
            if y.rank == x.rank:
                y.rank = y.rank + 1



