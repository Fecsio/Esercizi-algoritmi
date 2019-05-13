import math

from Lab3.Script.Distance import eucDistance
from Lab3.Script.Distance import geoDistance
import numpy as np



class Node:
    def __init__(self, id, coord1, coord2):
        self.id = id
        self.coord1 = coord1
        self.coord2 = coord2

    def __str__(self):
        s = "id: " + self.id + " coord1: " + str(self.coord1) + " coord2: " + str(self.coord2)
        return s

    def __repr__(self):
        s = "id: " + self.id + " coord1: " + str(self.coord1) + " coord2: " + str(self.coord2)
        return s

    def __eq__(self, other):
        return self.id == other.id

class Graph:
    def __init__(self, name, type, dimension):
        self.distMatrix = [[0 for x in range(int(dimension))] for y in range(int(dimension))]
        self.name = name
        self.type = type
        self.nodeNumber = 0

    def insertNodes(self, nodeList):
        for x in nodeList:
            id = int(x.id)
            for i in range(id-1, -1, -1):
                if self.type.strip() == "EUC_2D":
                    dist = eucDistance(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)
                    self.distMatrix[i][id - 1] = dist
                    self.distMatrix[id - 1][i] = dist
                else:
                    dist = geoDistance(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2) \
                        if x is not nodeList[i] else 0
                    self.distMatrix[i][id - 1] = dist
                    self.distMatrix[id - 1][i] = dist

    def getDistance(self, node1, node2):
        return self.distMatrix[node1-1][node2-1]

    def getOrderedEdges(self):
        edgeList = []
        k = 0
        for i in range(len(self.distMatrix)):
            for j in range(k, len(self.distMatrix[i])):
                edgeList.append(Edge(i, j, self.distMatrix[i][j]))
            k += 1

        return sorted(edgeList, key=lambda x: x.getWeight())

    def getDim(self):
        return len(self.distMatrix)



    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def getWeight(self):
        return self.weight






