from Lab4.Script.Contea import Contea
from Lab4.Script.HierarchicalClustering import euclidean_dist
from Lab4.Script.Parser import Parser
from Lab4.Script.ScatterPlotCluster import scatter_plot_cluster

def kmeans(P, k, q):
    n = len(P)
    sortedP = sorted(P, key=lambda c: c.population)  # sortedP = P ordinato secondo la popolazione
    centers = []
    for i in range(k):
        centers.append(sortedP[n-1-i])
        l = [0 for x in range(n)]
    for i in range(q):
        for j in range(n):
            l[j] = minDist(P[j], centers)
        centers = center(P, l, k)
    clusters = {c: [] for c in centers}
    for i in range(n):
        clusters[centers[l[i]]].append(P[i])
    return clusters





def minDist(P, centers):
    min = float('inf')
    index = None
    for c in range(len(centers)):
        dist = euclidean_dist((P.x, P.y), (centers[c].x, centers[c].y))
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

    def __str__(self):
        s = ("x: " + str(self.x) + " y: " + str(self.y))
        return s

    def __repr__(self):
        s = ("x: " + str(self.x) + " y: " + str(self.y))
        return s

L = Parser('unifiedCancerData_3108.csv')


lists = [Contea(0, 1, 1, 1, 0), Contea(1, 3, 2.5, 2, 0), Contea(2, 1.25, 3.75, 3, 0),
         Contea(3, 7, 2, 4, 0), Contea(4, 5, 6, 0, 0), Contea(5, 6.5, 5.5, 0, 0),
         Contea(6, 6, 6, 10, 0)]

clusters = kmeans(L, 15, 100)

scatter_plot_cluster(clusters, L)

