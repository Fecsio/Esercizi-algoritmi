from Lab3.Script.Graph import Graph
from Lab3.Script.Set import Set
from Lab3.Script.Set import Node
from Lab3.Script.Parser import Parser
from Lab3.Script.DepthFirstSearch import depthFirstSearch

# Visto che gli archi non vengono selezionati in successione è stata creata una struttura doppiamente linkata invece che
# una vera e propria struttura ad albero, l'algoritmo depthFirst si occupera di scorrere la struttura in maniera corretta
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.links = []
        self.linkNumber = 0

    def addLink(self, treeNode):
        self.links.append(treeNode)
        self.linkNumber += 1

    def getLinks(self):
        return self.links

    def getValue(self):
        return self.value

# Implementazione dell'algoritmo di kruskal
def Kruskal(Graph):
    # creazione della lista di archi ordinati per peso
    edgeList = Graph.getOrderedEdges()
    setList = Set()
    supTree = []
    treeIndex = -1
    maxLinks = 0
    minEdges = []
    # Creazione dei nodi che andrano a formare l'albero di supporto minimo
    for i in range(Graph.getDim()):
        supTree.append(TreeNode(i))

    # creazione dei set utilizzati per tenere traccia delle componeti connesse del grafo man mano che si aggiungono archi
    for i in range(Graph.getDim()):
        setList.makeSet(i)

    # Per ogni arco nella lista controlla se collega due set diversi e in quel caso unisce i set.
    # inoltre salva il nodo con più archi che poi verrà utilizzato come radice dell'albero
    for e in edgeList:
        node1 = setList.findSet(e.node1).getValue()
        node2 = setList.findSet(e.node2).getValue()
        if node1 != node2:
            minEdges.append(e.getWeight())
            supTree[e.node1].addLink(supTree[e.node2])
            supTree[e.node2].addLink(supTree[e.node1])
            index = -1
            localMax = 0
            if supTree[e.node2].linkNumber > supTree[e.node1].linkNumber:
                index = e.node2
                localMax = supTree[e.node2].linkNumber
            else:
                index = e.node1
                localMax = supTree[e.node1].linkNumber
            if localMax > maxLinks:
                treeIndex = index
                maxLinks = localMax
            setList.union(e.node1, e.node2)
    return supTree[treeIndex]


