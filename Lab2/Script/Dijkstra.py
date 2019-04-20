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

    suitable_edges = graph.edges[(s, t)]  # find all edges that connect s and t

    real_time = time.getTimeNoDay()
    """ we need to do this because param "time" could be plus one or more day,
    that means + 86400 seconds * more days;"""

    def lam(e):
        return e.times[0].seconds - real_time.seconds + e.weight
        # = journey time + difference between departure time and real_time, so real weight considering waiting time

    suitable_times = sorted({(e, lam(e)) for e in suitable_edges},
                            key=lambda x: lam(x[0]))
    """filter times in "suitable_edge" selecting only times with departure time greater or equal to real_time and
    order them by result of applying lam, from smallest to largest
    """

    suitable_times_same_day = list(filter(lambda x: x[0].times[0] >= real_time, suitable_times))
    # selecting departures at time after real_time, that means departures before 23:59 of the same day;

    if suitable_times_same_day:
        """If there are departures before the end of the day and after real_time..."""
        if (suitable_times[0][1] < 0 and suitable_times_same_day[0][1] <= suitable_times[0][1] + 86400) or \
                suitable_times[0][1] >= 0:
            """...the first of them is selected unless it's more convenient to wait and take a ride the day after; 
            it's time ( == result of applying lam) is returned together with the id of the associated edge and 
            it's departure and arrival time; """
            return suitable_times_same_day[0][0].id, suitable_times_same_day[0][0].times, suitable_times_same_day[0][1]
        """ (suitable_times_same_day[0].times[0].seconds - real_time.seconds +
                suitable_times_same_day[0].weight) # times[1].seconds - suitable_times_same_day[0].times[0].seconds)"""

    # else, the first suitable time is for sure the day after
    return suitable_times[0][0].id, suitable_times[0][0].times, (suitable_times[0][1] + 86400)
    """We add the number of seconds in a day because the result of the application of lam will be a 
    negative value as result of subtracting real_time (bigger) to first departure the day after, that will be smaller
    because it'calculated as it was the same day but indeed it's in the day after; 
    that first departure won't in fact be bigger than real_time because in that case we would have selected 
    it the day "before";"""


def relax(s, t, w, prevs, dists, times, temp_t, temp_l):
    """

    :param s: departure node
    :param t: arrival node
    :param w: weight of edge s -> t
    :param prevs: dictionary of previous nodes for each node
    :param dists: dictionary of distances from source node to each node
    :param times: dictionary of last times (departure, arrival) and lines used to reach each node
    :param temp_t: departure time, arrival time for edge s -> t
    :param temp_l: line selected for edge s -> t
    :return: nothing
    """
    dists[t] = dists[s] + w
    prevs[t] = s
    times[t] = [temp_t, temp_l]


def DijkstraSSSP(graph, sourceNodeId, time):
    """

    Dijkstra algorithm implementation

    :param graph: graph
    :param sourceNodeId: id of the node from which the algorithm has to find shortest path
    :return: prevs: dictionary with {keys = ids of all nodes; values = id of node that is
             predecessor of the node with id == key, in the minimum path starting from node with id == "sourceNodeId"}

             dists: dictionary with {keys = ids of all nodes; values = seconds that are necessary to reach the node with
             id == key, in the minimum path starting from node with id == "sourceNodeId"}

             times_and_lines: dictionary with {keys = ids of all nodes; values = lines
             and times (departure, arrival) in line used to reach node with id == key,
             in the minimum path starting from node with id == "sourceNodeId"}

    """
    assert sourceNodeId in graph.nodes.keys()

    # InitSSSP
    dists = {n: float("inf") for n in graph.nodes}  # all distances are infinite before starting to search minimum path
    prevs = {n: None for n in graph.nodes}  # all previous nodes are None before starting to search minimum path
    times_and_lines = {n: [None, None] for n in graph.nodes}  # no nodes are reached before starting to search minimum path

    dists[sourceNodeId] = 0

    # creating priority queue
    Q = BinaryHeap.BinaryHeap()
    for id_node in graph.nodes:
        Q.insertNode(id_node, dists[id_node])

    while len(Q.queue) > 0:  # the procedure stops when all nodes in the heap have been analyzed or...
        u = Q.extractMin()
        if dists[u] == float("inf"):  # ...when all remaining nodes are unreachable
            return prevs, dists, times_and_lines
        new_time = Time.Time()
        new_time.add_seconds(time.seconds + dists[u])
        # new_time = starting time + time required to reach u starting from source node;
        for v in graph.nodes[u].adj:
            if v != sourceNodeId:
                temp_line, temp_time, weight = w(graph, new_time, u, v)
                if dists[u] + weight < dists[v]:
                    relax(u, v, weight, prevs, dists, times_and_lines, temp_time, temp_line)
                    Q.decreaseKey(v, dists[v])

    return prevs, dists, times_and_lines


g = FileParser.FileParser()
t = Time.Time()
t.intTime(21, 30)
print(t)
p, d, tt = DijkstraSSSP(g, '200406015', t)

print("Predecessors:\n")
pprint.pprint(p)
print("\n")
print("Distances:\n")
pprint.pprint(d)
print("\n")
print("Best times (arriving to node from its previous), best line: \n")
pprint.pprint(tt)
print("\n")