import random

from Script import Node


def er_undirected(nodes, probability):
    if probability > 1:
        probability == 1
    elif probability < 0:
        probability == 0
    g = Node.Graph(nodes)
    for u in range(1, nodes+1):
        for v in range(1, nodes+1):
                a = random.uniform(0, 1)
                if a < probability:
                    g.addArc(u, v)
    return g.dict


n_nodes = int(input("Insert desired number of nodes: "))

p = float(input("Insert desired probability:"))

print(er_undirected(n_nodes, p))

