from collections import defaultdict
from Lab4.Script.HierarchicalClustering import euclidean_dist


def kmeans(P, k, q):
    sortedP = sorted(P, key=lambda c: c.population, reverse=True)  # sortedP = P ordinato secondo la popolazione

    centers = [(sortedP[i].x, sortedP[i].y) for i in range(k)]

    clusters = defaultdict(list)

    for i in range(q):
        clusters, points_sum = partition(P, centers)
        for j in range(k):
            x, y = points_sum[centers[j]]
            n = len(clusters[centers[j]])
            centers[j] = (x/n, y/n)

    return clusters


def partition(P, centers):
    # c = {i: [] for i in centers}  # dizionario con chiavi = centri, valori = lista di punti nel cluster con centro == chiave
    points_sum = {i: (0, 0) for i in centers}
    c = defaultdict(list)
    n = len(centers)

    for p in P:
        best_c = centers[0]
        best_dist = euclidean_dist((p.x, p.y), (centers[0][0], centers[0][1]))
        for i in range(1, n):
            tmp_dist = euclidean_dist((p.x, p.y), (centers[i][0], centers[i][1]))
            if tmp_dist < best_dist:
                best_dist = tmp_dist
                best_c = centers[i]
        c[best_c].append(p)
        points_sum[best_c] = (points_sum[best_c][0] + p.x, points_sum[best_c][1] + p.y)
    return c, points_sum
