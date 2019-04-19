import pprint
from Lab2.Script import FileParser
from Lab2.Script import BinaryHeap
from Lab2.Script import Time
from Lab2.Script.BinaryHeap import FastNode


def w(graph, time, s, t):
    """

    :param graph: graph
    :param time: time from which filtering departures
    :param s: departure node
    :param t: arrival node
    :return: the best time given by an edge that connect s and t at nearest time in respect
             of param "time"; it's the sum of the weight of that edge and the difference between
             edge's departure time and param "time"
    """

    # print("Arrivo: ", t, "Partenza: ", s)
    suitable_edge = graph.edges[(s, t)]  # find an edge that connects s and t

    # def lam(x): x[0].seconds - time.seconds + x[1].seconds - x[0].seconds
    print("In w, time:", time)
    really_suitable_edge = sorted({e for e in suitable_edge.times},
                                   key=lambda e: e[0].seconds - time.seconds + e[1].seconds - e[0].seconds)
    # filter times in "suitable_edge" selecting only times with departure time greater or equal to param "time" and
    # order them by best time (= journey time + difference between departure time and param "time")

    really_suitable_edges_pos = list(filter(lambda x: x[0] >= time, really_suitable_edge))

    # print(really_suitable_edge)
    if really_suitable_edges_pos:
        print("Partenze giorno stesso:", really_suitable_edges_pos)
        print("Parto alle: ", really_suitable_edges_pos[0][0], "arrivo alle: ", really_suitable_edges_pos[0][1])
        return really_suitable_edges_pos[0][0].seconds - time.seconds + really_suitable_edges_pos[0][1].seconds \
               - really_suitable_edges_pos[0][0].seconds
    print("Partenze:", really_suitable_edge)
    print("Parto alle: ", really_suitable_edge[0][0], "arrivo alle: ", really_suitable_edge[0][1])
    return really_suitable_edge[0][0].seconds - time.seconds + really_suitable_edge[0][1].seconds \
           - really_suitable_edge[0][0].seconds

def relax(s, t, w, prevs, dists):
    """

    :param s: departure node
    :param t: arrival node
    :param w: weight of edge s -> t
    :param prevs: list of previous nodes
    :param dists: list of distances
    :return: nothing
    """
    dists[t] = dists[s] + w
    prevs[t] = s


def DijkstraSSSP(graph, sourceNodeId, time):
    """

    Dijkstra algorithm implementation

    :param graph: graph
    :param sourceNode: node from which the algorithm has to find shortest path
    :return:

    """
    assert sourceNodeId in graph.nodes.keys()

    # InitSSSP
    dists = {n: float("inf") for n in graph.nodes}
    # print("~~~~~~~~~~ lunghezza dists:", len(dists))
    prevs = {n: None for n in graph.nodes}
    dists[sourceNodeId] = 0

    # creating priority queue
    Q = BinaryHeap.BinaryHeap()
    for id_node in graph.nodes:
        Q.insertNode(id_node, dists[id_node])
    # print("~~~~~~~~~~ lunghezza Q:", len(Q.queue))
    #print("~~ noice", Q)

    while len(Q.queue) > 0:
        u = Q.extractMin()
        if dists[u] == float("inf"):  # this means that all remaining nodes are unreachable
            print("AAAAA Nodi in coda: ", Q)
            return prevs, dists
        print("min=", u, " con dist:", dists[u])
        new_time = Time.Time("00000")
        new_time.add_seconds(time.seconds + dists[u])
        print("~~~~ adiacenti:", graph.nodes[u].adj)
        for v in graph.nodes[u].adj:
            print("v=", v)
            if v != sourceNodeId:
                weight = abs(w(graph, new_time, u, v))
                print("dist source to v prima: ", dists[v])
                print("weight + dist:", weight + dists[u], " at: ", u, "->", v)
                if dists[u] + weight < dists[v]:
                    print("dist source to u: ", dists[u])
                    #time.add_seconds(dists[u])
                    relax(u, v, weight, prevs, dists)
                    print("dist source to v: ", dists[v])
                    Q.decreaseKey(v, dists[v])
            print("\n")

    return prevs, dists


"""g = FileParser.FileParser()
t = Time.Time("00000")
t.intTime(13, 0)
print(t)
p, d = DijkstraSSSP(g, '500000079', t)

print("Predecessors:\n")
pprint.pprint(p)
print("Distances:\n")
pprint.pprint(d)"""
