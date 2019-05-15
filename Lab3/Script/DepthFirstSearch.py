from Lab3.Script.Graph import Graph

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.son = []

    def setParent(self, treeNode):
        self.parent = treeNode

    def addSon(self, treeNode):
        self.son.append(treeNode)

    def getParent(self):
        return self.parent

    def getSon(self):
        return self.son

    def getValue(self):
        return self.value

def listToTree(edgeList):
    nodeList = []
    for e in edgeList:
        present1 = False
        present2 = False
        for i in nodeList:
            if i.getValue() == e.node1:
                present1 = True
            if i.getValue() == e.node2:
                present2 = True
        if not present1:
            nodeList.append(TreeNode())


#def depthFirstSearch(Graph, tree):

