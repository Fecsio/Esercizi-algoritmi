import random
import pprint


from Script import Graph


def er_undirected(nodes, probability):
    if probability > 1:
        probability = 1
    elif probability < 0:
        probability = 0
    g = Graph.Graph(nodes)
    for u in range(1, nodes+1):
        for v in range(1, nodes+1):
                a = random.uniform(0, 1)
                if a < probability:
                    g.addArc(u, v)
    return g


n_nodes = int(input("Insert desired number of nodes: "))

p = float(input("Insert desired probability:"))

with open('../File vari/output.txt', 'w') as out:
    pprint.pprint(er_undirected(n_nodes, p).dict, stream=out)
