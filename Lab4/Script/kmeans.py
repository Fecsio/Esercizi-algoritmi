from collections import defaultdict
from Lab4.Script.HierarchicalClustering import euclidean_dist

def kmeans(P, k, q):
    n = len(P)
    sortedP = sorted(P, key=lambda c: c.population, reverse=True)  # sortedP = P ordinato secondo la

    centers = [(sortedP[i].x, sortedP[i].y) for i in range(k)]

    l = [-1 for x in range(n)]

    for i in range(q):
        for j in range(n):
            l[j] = minDist(P[j], centers)
        centers = center(P, l, k)

    clusters = defaultdict(list)
    for i in range(n):
        clusters[centers[l[i]]].append(P[i])
    return clusters

def minDist(P, centers):
    min = float('inf')
    index = None
    for c in range(len(centers)):
        dist = euclidean_dist((P.x, P.y), (centers[c][0], centers[c][1]))
        if dist < min:
            min = dist
            index = c
    return index


def center(P, l, k):
    centers = [(0, 0) for x in range(k)]
    count = [0 for x in range(k)]

    for i in range(len(P)):
        centers[l[i]] = (centers[l[i]][0] + P[i].x, centers[l[i]][1] + P[i].y)
        count[l[i]] += 1

    for c in range(k):
        centers[c] = (centers[c][0]/count[c], centers[c][1]/count[c])
    return centers


