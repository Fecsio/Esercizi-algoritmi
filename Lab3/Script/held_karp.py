import pprint

from Lab3.Script import Graph, Parser


def hk_visit(G, v, S, dists, prevs):

    if len(S) == 1:
        return G.getDistance(v, 1)

    elif dists[v - 1].get(S) is not None:
        return dists[v - 1][S]

    else:
        mindist = float("inf")
        minprec = None
        for n in S:
            if n != v:
                dist = hk_visit(G, n, S.difference([v]), dists, prevs) + G.getDistance(n, v)
                if dist < mindist:
                    mindist = dist
                    minprec = n
        dists[v - 1][S] = mindist
        prevs[v - 1][S] = minprec

        return mindist


def hk_tsp(G):
    dists = [dict() for n in range(0, len(G.distMatrix))]
    prevs = [dict() for n in range(0, len(G.distMatrix))]
    S = frozenset(range(1, len(G.distMatrix) + 1))
    a = hk_visit(G, 1, S, dists, prevs)
    pprint.pprint(dists)
    return a

glist = Parser.Parser()

print(hk_tsp(glist[1]))



