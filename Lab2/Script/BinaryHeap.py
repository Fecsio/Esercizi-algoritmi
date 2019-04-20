from Lab2.Script.Graph import Graph
import math

class FastNode:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance

    def getId(self):
        return self.id

    def getDistance(self):
        return self.distance

    def updateDistance(self, distance):
        self.distance = distance

    def __eq__(self, other):
        return other != None and self.id == other.id

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return str(self.id) + ' ' + str(self.distance)

    def max(node1, node2):
        if node1 > node2:
            return node1
        else:
            return node2

class BinaryHeap:
    def __init__(self):
        self.queue = [FastNode(0, 0)]

    def __str__(self):
        s = ""
        for e in self.queue:
            s += "(" + str(e.id) + ", " + str(e.distance) + ")\n"
        return s

    def getParentIndex(self, index):
        return math.floor(index/2)

    def getSxIndex(self, index):
        return index*2

    def getDxIndex(self, index):
        return index*2 + 1

    def parent(self, index):
        return self.queue[math.floor(index/2)]

    def sx(self, index):
        if index*2 > len(self.queue) - 1:
            return None
        return self.queue[index*2]

    def dx(self, index):
        if index*2 + 1 > len(self.queue) - 1:
            return None
        return self.queue[index*2 + 1]

    def getNode(self, index):
        return self.queue[index]

    def put(self, element, index):
        self.queue[index]

    def insertNode(self, nodeId, nodeDistance):
        heapSize = self.queue.__len__()
        if heapSize == 1:
            self.queue.append(FastNode(nodeId, nodeDistance))
        else:
            self.queue.append(FastNode(nodeId, nodeDistance))
            i = heapSize
            while i > 1 and self.parent(i) > self.getNode(i):
                temp = self.getNode(i)
                self.queue.pop(i)
                self.queue.insert(i, self.parent(i))
                self.queue.pop(self.getParentIndex(i))
                self.queue.insert(self.getParentIndex(i), temp)
                i = self.getParentIndex(i)

    def decreaseKey(self, id, distance):
        i = 0
        i = self.queue.index(FastNode(id, 0))
        self.queue[i].updateDistance(distance)
        if i > 0:
            while i > 1 and self.parent(i) > self.getNode(i):
                temp = self.getNode(i)
                self.queue.pop(i)
                self.queue.insert(i, self.parent(i))
                self.queue.pop(self.getParentIndex(i))
                self.queue.insert(self.getParentIndex(i), temp)
                i = self.getParentIndex(i)

    def extractMin(self):
        returnValue = self.queue.pop(1)
        self.queue.insert(1, self.queue.pop(len(self.queue) - 1))
        i = 1
        while i < len(self.queue) and self.sx(i) is not None and self.dx(i) is not None and (self.getNode(i) > self.sx(i) or self.getNode(i) > self.dx(i)):
            sx = self.sx(i)
            dx = self.dx(i)
            if sx < dx:
                sxIndex = self.getSxIndex(i)
                temp = self.queue.pop(i)
                self.queue.insert(i, sx)
                self.queue.pop(sxIndex)
                self.queue.insert(sxIndex, temp)
                i = sxIndex
            else:
                dxIndex = self.getDxIndex(i)
                temp = self.queue.pop(i)
                self.queue.insert(i, dx)
                self.queue.pop(dxIndex)
                self.queue.insert(dxIndex, temp)
                i = dxIndex
        return returnValue.id


