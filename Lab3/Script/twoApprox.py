from Lab3.Script.Kruskal import Kruskal
from Lab3.Script.DepthFirstSearch import depthFirstSearch

def twoApprox(graph):
    print("2-approx")
    tree = Kruskal(graph)
    orderedList = []
    pathWeight = depthFirstSearch(graph, tree, orderedList, -1)
    print(pathWeight)
    return pathWeight


