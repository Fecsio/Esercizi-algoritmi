from Lab3.Script.Kruskal import Kruskal
from Lab3.Script.DepthFirstSearch import depthFirstSearch

def twoApprox(graph):

    tree = Kruskal(graph)
    orderedList = []
    pathWeight = depthFirstSearch(graph, tree, orderedList, -1)
    return pathWeight


