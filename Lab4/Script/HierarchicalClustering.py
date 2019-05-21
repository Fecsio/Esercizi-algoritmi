from Lab4.Script import Parser
from Lab4.Script import Contea
import pprint
import math

class Centroid:
    def __init__(self, points):
        x, y = 0, 0

        for p in points:
            x +=p.x
            y +=p.y

        self.x = x/len(points)
        self.y = y/len(points)

    def __str__(self):
        s = ("x: " + str(self.x) + " y: " + str(self.y))
        return s

    def __repr__(self):
        s = ("x: " + str(self.x) + " y: " + str(self.y))
        return s

def h_clustering(P, k):
    n = len(P)
    sortedP = sorted(P, key=lambda c: c.x)  # sortedP = P ordinato secondo la coordinata x
    centers = list(Centroid([p]) for p in sortedP)

    print(centers)

    while len(centers) > k:
        S = [i for i in range(0, len(centers))]
        S.sort(key=lambda i: centers[i].y)  # S = lista degli indici i di P ordinati per coordinata y di P[i]

        _, i, j = slow_closest_pair(centers) # range(0, len(centers)), centers, S)
        print("+ vicini: ", i, j)
        prev_i, prev_j = centers[i], centers[j]
        centers[i] = Centroid([centers[i], centers[j]])
        centers.remove(prev_j)
        print(centers)

        # clusters.add(Centroid(clusters))


    

"""
    clusters = set(tuple([p]) for p in P)
    pprint.pprint(clusters)
    while len(clusters) > k:
        i, j = fast_closest_pair(
        clusters.add(tuple([P[i], P[j]]))
        try:
            clusters.remove(tuple([P[i]]))
            clusters.remove(tuple([P[j]]))
        except KeyError:
            return clusters
    return clusters
"""

# ~~~~~~~~~~~~~~~ funziona ~~~~~~~~~~~~~~~

def slow_closest_pair(P):
    """
    :param P: insieme di punti dove ogni punto pi è un oggetto Contea (con coordinate x e y)
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P e i, j sono gli indici di
    due punti la cui distanza è d
    """
    d, i, j = float("inf"), -1, -1
    for u in range(0, len(P)-1):
        for v in range(u + 1, len(P)-1):
            new_d = euclidean_dist(P[u], P[v])
            if new_d < d:
                d = new_d
                i = u
                j = v
    return d, i, j

# ~~~~~~~~~~~~~~~ funziona ~~~~~~~~~~~~~~~

def split(S, Pl):
    """
    :param S: vettore ordinato
    :param Pl: partizione sinistra degli elementi in S
    :return: Due vettori Sl e Sr ordinati che contengono rispettivamente gli elementi in Pl e Pr
    """

    # print("In split")
    # print("len(S):", len(S))
    # print("len(Pl):", len(Pl))
    Sl = []
    Sr = []
    pprint.pprint(Pl)
    pprint.pprint(S)
    for i in range(0, len(S)):
        if S[i] in Pl:
            Sl.append(S[i])
        else:
            Sr.append(S[i])
    # print("len(Sl):", len(Sl))
    # print("len(Sr):", len(Sr))
    return Sl, Sr

# ~~~~~~~~~~~~~~~ non funziona ~~~~~~~~~~~~~~~


def fast_closest_pair(p_indxs, P, S):
    """
    :param P: insieme di punti dove ogni punto pi è un oggetto Contea (con coordinate x e y), ordinati per coordinata x crescente
    :param S: vettore con gli indici 0...n-1 ordinati per coordinata y crescente
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P e i, j sono gli indici di
    due punti la cui distanza è d
    """
    n = len(p_indxs)

    if n <= 3:
        return slow_closest_pair(P)

    m = math.floor(n/2)
    Pl = [i for i in p_indxs[:m]]
    Pr = [i for i in p_indxs[m:n]]

    Sl, Sr = split(S, Pl)

    d, i, j = min(fast_closest_pair(Pl, P, Sl), fast_closest_pair(Pr, P, Sr))
    mid = 0.5*(P[m-1].x + P[m].x)
    d2, i2, j2 = closest_pair_strip(P, S, mid, d)
    if d2 < d:
        return d2, i2, j2
    return d, i, j

# ~~~~~~~~~~~~~~~ non funziona ~~~~~~~~~~~~~~~


def closest_pair_strip(P, S, mid, d):
    """
    :param P: insieme di punti dove ogni punto pi è un oggetto Contea (con coordinate x e y), ordinati per coordinata x crescente
    :param S: vettore con gli indici 0...n-1 ordinati per coordinata y crescente
    :param mid: valore reale
    :param d: valore reale positivo
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P che si trovano nella fascia verticale
    [mid - d, mid + d] e i, j sono gli indici di due punti la cui distanza è d
    """
    S1 = []
    for i in range(0, len(S)):
        if abs(P[S[i]].x - mid) < d:
            S1.append(S[i])
    d, i, j = float('inf'), -1, -1
    for u in range(0, len(S1) - 2):
        for v in range(u + 1, min(u + 5, len(S1) - 1)):
            new_d = euclidean_dist(P[S1[u]], P[S1[v]])
            if new_d < d:
                d = new_d
                i = S1[u]
                j = S1[v]
    return d, i, j


def euclidean_dist(c1, c2):
    return math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)


L = Parser.Parser()
#C = h_clustering(list(set().union(*(l for l in L))), 5)

"""for l in L[3]:
    print(str(l.id) + "," + str(l.x) + "," + str(l.y))"""
lists = [Contea.Contea(0, 1, 1, 0, 0), Contea.Contea(1, 3, 2.5, 0, 0), Contea.Contea(2, 1.25, 3.75, 0, 0),
         Contea.Contea(3, 7, 2, 0, 0), Contea.Contea(4, 5, 6, 0, 0), Contea.Contea(5, 6.5, 5.5, 0, 0),
         Contea.Contea(6, 6, 6, 0, 0)]

for c in lists:
    print(str(c) + " x: " + str(c.x) + " y: " + str(c.y))

print("")
h_clustering(lists, 3)
"""lists = [Contea.Contea(0, 1, 1, 0, 0), Contea.Contea(1, 3, 2.5, 0, 0), Contea.Contea(2, 1, 4, 0, 0),
         Contea.Contea(3, 7, 2, 0, 0), Contea.Contea(4, 5, 6, 0, 0), Contea.Contea(5, 6.5, 5.5, 0, 0),
         Contea.Contea(6, 6, 6, 0, 0)]


S = sorted([i for i in range(0, len(lists))], key=lambda c: lists[c].y)  # ok
lists.sort(key=lambda c: c.x)  # ok

m = math.floor(len(lists) / 2)

mid = 0.5 * (lists[m - 1].x + lists[m].x)

d = 3

d, i, j = closest_pair_strip(lists, S, mid, d)

print(i,j)
print(lists[i], lists[j])

# S = [0, 1, 4, 5, 9, 10, 12]
m = math.floor(len(S) / 2)
Pl = [S[i] for i in range(0, m)]
Pr = [S[i] for i in range(m, len(S))]

Sl, Sr = split(S, Pl)
pprint.pprint(S)
pprint.pprint(Sl)
pprint.pprint(Sr)

# C = h_clustering(list(L[2]), 7)

# pprint.pprint(C)

"""