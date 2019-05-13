from Lab3.Script.Graph import Graph
from Lab3.Script.Set import Set
from Lab3.Script.Set import Node
from Lab3.Script.Parser import Parser



def Kruskal(Graph):
    edgeList = Graph.getOrderedEdges()
    print(len(edgeList))
    setList = Set()
    supTree = []
    for i in range(Graph.getDim()):
        setList.makeSet(i)
    for e in edgeList:
        if setList.findSet(e.node1).getValue() != setList.findSet(e.node2).getValue():
            supTree.append(e)
            setList.union(e.node1, e.node2)
    return supTree

g = Parser()
print("grafi:", g)
set = Kruskal(g[0])
print("length:", len(set))
for e in set:
    print('{'+str(e.node1), str(e.node2)+'}',)


