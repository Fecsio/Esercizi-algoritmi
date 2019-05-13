
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent.getValue()

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

class Set:
    def __init__(self):
        self.leader = None
        self.rank = 0

    def makeSet(self, node):
        self.leader = Node(node)
        self.leader.setParent(self.leader)

    def findSet(self, node):
        parent = node.getParent()
        if parent != node.getValue():
            parent.setParent(self.findSet(parent))
        return parent

    def union(self, set1, set2):
        
