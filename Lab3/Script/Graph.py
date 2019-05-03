from Lab3.Script.Distance import eucDistance


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
        print("xD?")
        for x in nodeList:
            print("xD??")
            for i in range(x.id-1, 0):
                if self.type == "EUC_2D":
                    print("xD", self.distMatrix[i][x.id-1])
                    dist = eucDistance(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)
                    self.distMatrix[i][x.id - 1] = dist
                    self.distMatrix[x.id - 1][i] = dist
                #else:
                    #self.distMatrix = geoDist(x.coord1, x.coord2, nodeList[i].coord1, nodeList[i].coord2)






