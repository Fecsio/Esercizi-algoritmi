from Lab3.Script.Distance import eucDistance
from Lab3.Script.Distance import geoDistance



class Node:
    def __init__(self, id, coord1, coord2):
        self.id = id
        self.coord1 = coord1
        self.coord2 = coord2


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
                    dist = geoDistance(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)
                    self.distMatrix[i][id - 1] = dist
                    self.distMatrix[id - 1][i] = dist

    def getDistance(self, node1, node2):
        return self.distMatrix[node1-1][node2-1]






