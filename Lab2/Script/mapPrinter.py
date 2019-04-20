import matplotlib.pyplot as plt
from Lab2.Script.Graph import Graph
import re
from Lab2.Script.Time import Time

def mapPrinter(graph, predecessors, lines, destination, departureTime):
    #print(lines)
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
    for n in path:
        pathLat.append(graph.nodes[n].getLat())
        pathLng.append(graph.nodes[n].getLng())
    i = len(path) - 2
    changes = []
    currentBus = lines[path[i]][1]
    el = 0
    arrivalTime = None
    while i >= 0:
        current = path[i]
        prev = path[i+1]
        if i == len(path) -2:
            currentBus = lines[current][1]
            run = lines[current][1][len(lines[current][1])-5:]
            lineId = lines[current][1][0:len(lines[current][1])-5]
            changes.append(lines[current][0][0].getTime() + " : run " + run + " " + lineId + " from " + prev + " to ")
        elif i == 0:
            changes[el] += current
            arrivalTime = lines[current][0][1].getTime()
        elif currentBus != lines[current][1]:
            run = lines[current][1][len(lines[current][1]) - 5:]
            lineId = lines[current][1][0:len(lines[current][1]) - 5]
            currentBus = lines[current][1]
            changes[el] += prev
            el += 1
            changes.append(lines[current][0][0].getTime() + " : run " + run + " " + lineId + " from " + prev + " to ")
        i -= 1
    print("Traveling form " + path[len(path)-1] + " to " + path[0])
    print("Departure time: " + departureTime)
    print("Arrival time: " + arrivalTime)
    for s in changes:
        print(s)
    plt.plot(pathLng, pathLat, zorder=10)
    plt.plot(posLng, posLat, linestyle="none", marker="o", markersize=1, color="gray", zorder=1)
    plt.axis('off')
    plt.savefig("../File vari/Immagini/" + path[len(path)-1] + "to" + path[0] + ".png")
    plt.show()



