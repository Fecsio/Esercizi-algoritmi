import pprint
from Lab2.Script import FileParser
from Lab2.Script import BinaryHeap
from Lab2.Script import Time


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

    suitable_edge = graph.edges[(s, t)]  # find an edge that connects s and t

    real_time = time.getTimeNoDay()  # we need to do this because param "time" could be plus one or more day,
    # so + 86400 seconds * more days;

    suitable_times = sorted({e for e in suitable_edge.times},
                            key=lambda e: e[0].seconds - real_time.seconds + e[1].seconds - e[0].seconds)
    # filter times in "suitable_edge" selecting only times with departure time greater or equal to real_time and
    # order them by best time (= journey time + difference between departure time and param "time");

    suitable_times_pos = list(filter(lambda x: x[0] >= real_time, suitable_times))  # selecting
    # departures at time after real_time, that means departures before 23:59 of the same day;

    if suitable_times_pos:  # if there are departures before the end of the day and after real_time,
        # the first of them (that will be the best because they have been sorted before)
        # is selected and it's time (journey time + difference between departure time and real_time) is returned;
        return suitable_times_pos[0][0].seconds - real_time.seconds + suitable_times_pos[0][1].seconds \
               - suitable_times_pos[0][0].seconds

    # else, the first suitable time is the day after
    return (suitable_times[0][0].seconds - real_time.seconds + suitable_times[0][1].seconds -
            suitable_times[0][0].seconds) + 86400  # we add the number of seconds in a day because the result of the
    # calculus between parenthesis will be a negative value as result of subtracting real_time (bigger)
    # to first departure the day after, that will be smaller because it'calculated as it was the same day but
    # indeed it's in the day after; that first departure won't in fact be bigger than real_time because in
    # that case we would have selected it the day "before";


def relax(s, t, w, prevs, dists):
    """

    :param s: departure node
    :param t: arrival node
    :param w: weight of edge s -> t
    :param prevs: dictonary of previous nodes
    :param dists: dictonary of distances
    :return: nothing
    """
    dists[t] = dists[s] + w
    prevs[t] = s


def DijkstraSSSP(graph, sourceNodeId, time):
    """

    Dijkstra algorithm implementation

    :param graph: graph
    :param sourceNode: node from which the algorithm has to find shortest path
    :return: prevs: dictionary with {keys = ids of all nodes; values = id of node that is
             predecessor of the node with id == key, in the minimum path starting from node with id == "sourceNodeId"}

             dists: dictionary with {keys = ids of all nodes; values = seconds that are necessary to reach the node with
             id == key, in the minimum path starting from node with id == "sourceNodeId"}

    """
    assert sourceNodeId in graph.nodes.keys()

    # InitSSSP
    dists = {n: float("inf") for n in graph.nodes}
    prevs = {n: None for n in graph.nodes}
    dists[sourceNodeId] = 0

    # creating priority queue
    Q = BinaryHeap.BinaryHeap()
    for id_node in graph.nodes:
        Q.insertNode(id_node, dists[id_node])

    while len(Q.queue) > 0:  # the procedure stops when all nodes in the heap have been analyzed or...
        u = Q.extractMin()
        if dists[u] == float("inf"):  # ...when all remaining nodes are unreachable
            return prevs, dists
        new_time = Time.Time()
        new_time.add_seconds(time.seconds + dists[u])  # new_time = starting time + time required to reach u
        # starting from source node;
        for v in graph.nodes[u].adj:
            if v != sourceNodeId:
                weight = w(graph, new_time, u, v)
                if dists[u] + weight < dists[v]:
                    relax(u, v, weight, prevs, dists)
                    Q.decreaseKey(v, dists[v])

    return prevs, dists


g = FileParser.FileParser()
t = Time.Time()
t.intTime(13, 0)
print(t)
p, d = DijkstraSSSP(g, '500000079', t)

print("Predecessors:\n")
pprint.pprint(p)
print("Distances:\n")
pprint.pprint(d)
