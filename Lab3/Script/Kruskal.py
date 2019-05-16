from Lab3.Script.Graph import Graph
from Lab3.Script.Set import Set
from Lab3.Script.Set import Node
from Lab3.Script.Parser import Parser
from Lab3.Script.DepthFirstSearch import depthFirstSearch

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.links = []

    def addLink(self, treeNode):
        self.links.append(treeNode)

    def getLinks(self):
        return self.links

    def getValue(self):
        return self.value

def Kruskal(Graph):
    edgeList = Graph.getOrderedEdges()
    setList = Set()
    supTree = []
    for i in range(Graph.getDim()):
        supTree.append(TreeNode(i))
    for i in range(Graph.getDim()):
        setList.makeSet(i)
    for e in edgeList:
        node1 = setList.findSet(e.node1).getValue()
        node2 = setList.findSet(e.node2).getValue()
        if node1 != node2:
            supTree[e.node1].addLink(supTree[e.node2])
            supTree[e.node2].addLink(supTree[e.node1])
            setList.union(e.node1, e.node2)
    return supTree[0]

g = Parser()
print("grafi:", g)
tree = Kruskal(g[0])
orderedList = []
depthFirstSearch(g[0], tree, orderedList, -1)
count = 0
"""for e in edgeList:
    print('{'+str(e.node1), str(e.node2)+'}', "w="+str(e.weight))
    if count == 12:
        print("----")
    count+=1
listToTree(edgeList)"""

