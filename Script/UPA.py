import random
from Script import Graph
import pprint


def UPA(n, m):

    numNodes = m
    nodeNumbers = []
    """n = 6474    # da configurare
    m = 2       # da configurare (metà del valore medio del grado dei nodi da grafo costruito dai dati)
    """

    graph = Graph.Graph(m)
    createCompleteGraph(m, graph)
    DPAtrial(m, nodeNumbers)  # ok
    for node1 in range(m, n+1):
        pulled = runTrial(m, nodeNumbers, numNodes)
        numNodes += 1
        graph.addNode(node1)
        for node2 in range(0, len(pulled)):
            graph.addArc(node1, pulled[node2])

    return graph

    """pprint.pprint(graph.dict) --- funziona anche così BTW ---
    print(graph.countNodes())
    print(graph.countArcs())"""



# Crea la prima "urna" per l'aggiunta di nuovi nodi
def DPAtrial(init, nodeNumbers):
    for node in range(1, init+1):
        nodeNumbers.append(node)


# Crea un grafo completo con m nodi
def createCompleteGraph(init, graph):
    for nodeInit1 in range(1, init+1):
        for nodeInit2 in range(1, init+1):
            graph.addArc(nodeInit1, nodeInit2)


def runTrial(init, nodeNumbers, numNodes):
    newPulled = []
    #print(nodeNumbers)
    for node in range(1, init+1):
        pulledNode = random.choice(nodeNumbers)
        newPulled.append(pulledNode)
    nodeNumbers.append(numNodes)
    nodeNumbers.extend(newPulled)
    return newPulled



