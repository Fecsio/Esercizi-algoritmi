from Lab4.Script.Contea import Contea
from Lab4.Script.HierarchicalClustering import Centroid
from Lab4.Script.HierarchicalClustering import euclidean_dist
from Lab4.Script.Parser import Parser

def kmenas(P, k, q):
    n = len(P)
    sortedP = sorted(P, key=lambda c: c.population)  # sortedP = P ordinato secondo la popolazione
    centers = []
    for i in range(k):
        centers.append(sortedP[n-1-i])
        l = [0 for x in range(n)]
    for i in range(q):
        for j in range(n):
            l[i] = minDist(P[i], centers)
        centers = center(P, l, k)
    print(centers)
    return l





def minDist(P, centers):
    min = float('inf')
    index = None
    for c in range(len(centers)):
        dist = euclidean_dist(P, centers[c])
        if dist < min:
            min = dist
            index = c
    return index


def center(P, l, k):
    centers = [Point(0, 0) for x in range(k)]
    count = [0 for x in range(k)]
    for i in range(len(P)):
        centers[l[i]].x += P[i].x
        centers[l[i]].y += P[i].y
        count[l[i]] += 1
    for c in range(k):
        centers[c].x /= count[c]
        centers[c].y /= count[c]
    return centers


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

L = Parser()


lists = [Contea(0, 1, 1, 1, 0), Contea(1, 3, 2.5, 2, 0), Contea(2, 1.25, 3.75, 3, 0),
         Contea(3, 7, 2, 4, 0), Contea(4, 5, 6, 0, 0), Contea(5, 6.5, 5.5, 0, 0),
         Contea(6, 6, 6, 10, 0)]

kmenas(lists, 3, 1)