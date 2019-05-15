from Lab3.Script.Graph import Graph
from Lab3.Script.Set import Set
from Lab3.Script.Set import Node
from Lab3.Script.Parser import Parser
from Lab3.Script.DepthFirstSearch import listToTree



def Kruskal(Graph):
    edgeList = Graph.getOrderedEdges()
    print(len(edgeList))
    setList = Set()
    supTree = []
    for i in range(Graph.getDim()):
        setList.makeSet(i)
    for e in edgeList:
        node1 = setList.findSet(e.node1).getValue()
        node2 = setList.findSet(e.node2).getValue()
        if node1 != node2:
            supTree.append(e)
            setList.union(e.node1, e.node2)
    return supTree

g = Parser()
print("grafi:", g)
edgeList = Kruskal(g[0])
count = 0
for e in edgeList:
    print('{'+str(e.node1), str(e.node2)+'}', "w="+str(e.weight))
    if count == 12:
        print("----")
    count+=1
listToTree(edgeList)

