


class Node:
    def __init__(self, id, coord1, coord2):
        self.id = id
        self.coord1 = coord1
        self.coord2 = coord2


class Graph:
    def __init__(self, name, type, dimension):
        self.distMatrix = [[0 for x in range(dimension)] for y in range(dimension)]
        self.name = name
        self.type = type
        self.nodeNumber = 0

    def insertNodes(self, nodeList):
        for x in nodeList:
            for i in range(x.id-1, 0):
                if self.type == "GEO":
                    self.distMatrix = geoDistance(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)
                else:
                    self.distMatrix = euDist(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)





