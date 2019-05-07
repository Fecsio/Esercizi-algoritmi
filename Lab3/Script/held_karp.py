import multiprocessing
import pprint
import sys
import time

from Lab3.Script import Graph, Parser


def hk_visit(G, v, S, dists, prevs, timeout):

    timed_out = False

    if len(S) == 1:
        return G.getDistance(v, 1), False

    elif dists[v - 1].get(S) is not None:
        return dists[v - 1][S], False

    else:
        mindist = float("inf")
        minprec = None
        for n in S:
            if n != v:
                dist, t_o = hk_visit(G, n, S.difference([v]), dists, prevs, timeout)
                dist += G.getDistance(n, v)

                if dist < mindist:
                    mindist = dist
                    minprec = n

                if t_o or time.time() > timeout:
                    timed_out = True
                    break

        dists[v - 1][S] = mindist
        prevs[v - 1][S] = minprec
        return mindist, timed_out


def hk_tsp(G, timeout):
    dists = [dict() for n in range(0, len(G.distMatrix))]
    prevs = [dict() for n in range(0, len(G.distMatrix))]
    S = frozenset(range(1, len(G.distMatrix) + 1))

    start = time.time()
    r, t_o = hk_visit(G, 1, S, dists, prevs, time.time() + timeout)

    return r, t_o, time.time() - start
