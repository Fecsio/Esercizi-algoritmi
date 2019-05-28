from Lab4.Script.utils import *


def h_clustering(P, k, pre_processed):
    """
     Algoritmo di clustering gerarchico agglomerativo

    :param P: lista di oggetti di tipo Contea (con coordinate x e y) oppure
            un dizionario di cluster pre calcolati (con pre_processed = True)
    :param k: numero di cluster in cui dividere l'insieme P
    :param pre_processed: TRUE sse viene passato in P un dizionario di cluster pre calcolati
    :return:
    """

    if not pre_processed:
        clusters = {(p.x, p.y): [p] for p in P}

    else:
        clusters = P

    while len(clusters) > k:

        centers = clusters.keys()

        points = sorted(centers, key=lambda k: k[0])
        S = sorted(centers, key=lambda k: k[1])

        _, i, j = fast_closest_pair(points, S)

        # _, i, j = slow_closest_pair(points)

        clusters[calc_center(clusters[i]+clusters[j])] = clusters[i]+clusters[j]
        clusters.pop(i)
        clusters.pop(j)

    return clusters


def slow_closest_pair(P):
    """
    :param P: insieme di punti dove ogni punto pi è una coppia di coordinate x e y
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P e i, j sono gli indici (cioè le coordinate)
     di due punti la cui distanza è d
    """
    n = len(P)

    d, i, j = float("inf"), -1, -1
    for u in range(0, n):
        for v in range(u + 1, n):
            new_d = euclidean_dist(P[u], P[v])
            if new_d < d:
                d = new_d
                i = P[u]
                j = P[v]
    return d, i, j


def split(S, Pl):
    """
    :param S: vettore ordinato
    :param Pl: partizione sinistra degli elementi in S
    :return: Due vettori Sl e Sr ordinati che contengono rispettivamente gli elementi in Pl e Pr
    """
    Sl = []
    Sr = []
    for i in range(0, len(S)):
        if S[i] in Pl:
            Sl.append(S[i])
        else:
            Sr.append(S[i])
    return Sl, Sr


def fast_closest_pair(P, S):
    """
    :param P: insieme di punti dove ogni punto pi è una coppia di coordinate x e y, ordinate per coordinata x crescente
    :param S: vettore con le coppie di coordinate x e y in P, ordinate per coordinata y crescente
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P e i, j sono gli indici di
    due punti la cui distanza è d
    """
    n = len(P)

    if n <= 3:
        return slow_closest_pair(P)

    m = math.floor(n/2)
    Pl = [i for i in P[:m]]
    Pr = [i for i in P[m:n]]

    Sl, Sr = split(S, Pl)

    d, i, j = min(fast_closest_pair(Pl, Sl), fast_closest_pair(Pr, Sr))

    mid = 0.5*(P[m-1][0] + P[m][0])

    d2, i2, j2 = closest_pair_strip(S, mid, d)

    if d2 < d:
        return d2, i2, j2

    return d, i, j


def closest_pair_strip(S, mid, d):
    """
    :param P: insieme di punti dove ogni punto pi è una coppia di coordinate x e y, ordinate per coordinata x crescente
    :param S: vettore con le i punti in P, ordinati per coordinata y crescente
    :param mid: valore reale
    :param d: valore reale positivo
    :return: d, i, j dove d è la più piccola distanza tra coppie di punti in P che si trovano nella fascia verticale
    [mid - d, mid + d] e i, j sono gli indici di due punti la cui distanza è d
    """
    n = len(S)
    S1 = []
    for i in range(0, n):
        if abs(S[i][0] - mid) < d:
            S1.append(S[i])

    d, i, j = float('inf'), -1, -1
    k = len(S1)
    for u in range(0, k - 1):
        for v in range(u + 1, min(u + 4, k)):
            new_d = euclidean_dist(S1[u], S1[v])
            if new_d < d:
                d = new_d
                i = S1[u]
                j = S1[v]
    return d, i, j

