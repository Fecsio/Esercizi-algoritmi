from collections import defaultdict
from Lab4.Script.utils import *


def kmeans(P, k, q):
    sortedP = sorted(P, key=lambda c: c.population, reverse=True)  # sortedP = P ordinato secondo la popolazione

    centers = [(sortedP[i].x, sortedP[i].y) for i in range(k)]

    clusters = defaultdict(list)

    for i in range(q):
        clusters = partition(P, centers)
        if i == q-1:
            old_centers = centers.copy()
        for j in range(k):
            centers[j] = calc_center(clusters[centers[j]])

    for i in range(k):
        clusters[centers[i]] = clusters[old_centers[i]]
        if centers[i] != old_centers[i]:
            del clusters[old_centers[i]]

    return clusters

def partition(P, centers):
    c = {i: [] for i in centers}  # dizionario con chiavi = centri, valori = lista di punti nel cluster con centro == chiave
    n = len(c)

    for p in P:
        best_c = centers[0]
        best_dist = euclidean_dist((p.x, p.y), (centers[0][0], centers[0][1]))
        for i in range(1, n):
            tmp_dist = euclidean_dist((p.x, p.y), (centers[i][0], centers[i][1]))
            if tmp_dist < best_dist:
                best_dist = tmp_dist
                best_c = centers[i]
        c[best_c].append(p)
    return c
