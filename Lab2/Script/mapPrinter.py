import matplotlib.pyplot as plt
from Lab2.Script.Graph import Graph

def mapPrinter(graph, predecessors, destination):
    posLng = []
    posLat = []
    pathLng = []
    pathLat = []
    for n in graph.nodes:
        posLng.append(graph.nodes[n].getLng())
        posLat.append(graph.nodes[n].getLat())
    path = []
    pred = destination
    while(pred):
        path.append(pred)
        pred = predecessors[pred]
    print("Path:", path)
    for n in path:
        pathLat.append(graph.nodes[n].getLat())
        pathLng.append(graph.nodes[n].getLng())
    plt.plot(pathLng, pathLat, zorder=10)
    plt.plot(posLng, posLat, linestyle="none", marker="o", markersize=1, color="gray", zorder=1)
    plt.axis('off')
    plt.show()


