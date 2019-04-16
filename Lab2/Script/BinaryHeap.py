from Lab2.Script.Nodo import Graph
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
        return self.id == other.id

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
        return self.queue[index*2]

    def dx(self, index):
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
        """        for e in self.queue:
            if e.getId() == id:
                i = self.queue.index()
                e.updateDistance(distance)
                break"""
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
        while i < len(self.queue) and (self.getNode(i) > self.sx(i) or self.getNode(i) > self.dx(i)):
            sx = self.sx(i)
            dx = self.dx(i)
            if sx < dx:
                sxIndex = self.getSxIndex(i)
                temp = self.queue.pop(i)
                self.queue.insert(i, sx)
                self.queue.pop(sxIndex)
                self.queue.insert(sxIndex, temp)
            else:
                dxIndex = self.getDxIndex(i)
                temp = self.queue.pop(i)
                self.queue.insert(i, dx)
                self.queue.pop(dxIndex)
                self.queue.insert(dxIndex, temp)
        return returnValue.id


"""
PRINT IS THE BEST DEBUGGER
n1 = FastNode(1, 123)
n2 = FastNode(2, 23)
n3 = FastNode(3, 13)
n4 = FastNode(4, 12)
n5 = FastNode(5, 8)

Q = BinaryHeap()
Q.insertNode(n1.getId(), n1.getDistance())
Q.insertNode(n2.getId(), n2.getDistance())
Q.insertNode(n3.getId(), n3.getDistance())
Q.insertNode(n4.getId(), n4.getDistance())
Q.insertNode(n5.getId(), n5.getDistance())
Q.decreaseKey(1, 2)
Q.decreaseKey(2, 1)
print(Q.extractMin())
print(Q)"""


