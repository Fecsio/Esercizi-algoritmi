from Lab3.Script.Parser import Parser
from Lab3.Script import held_karp
from Lab3.Script.twoApprox import twoApprox
from Lab3.Script import constructive_heuristic as ch
import time




graph_list = Parser()
best_sol = [134602, 21294, 7013, 3323, 426, 18659688, 35002]
# [0]: gr229.tsp,
# [1]: kroD100.tsp,
# [2]: ulysses22.tsp,
# [3]: burma12.tsp,
# [4]: eil51.tsp,
# [5]: dsj1000.tsp,
# [6]: d493.tsp
minTime = 0
minLenght = float("inf")
minTour = []
for i in range(0,100):
    tour, time, lenght = ch.insertion_algorithm(graph_list[6])
    if(lenght < minLenght):
        minLenght = lenght
        minTime = time
        minTour = tour
print("Tour:", minTour, "\nLenght:", minLenght, "\nTime:", minTime)

"""
for i in range(0, 7):
    try:
        start = time.time()
        val = twoApprox(graph_list[i])
        print("\nSolution for graph ", graph_list[i], ": " + str(val), " time: ", round(time.time()-start, 2), "with error =", round(100*(val - best_sol[i]) / best_sol[i], 2), "%")

    except IOError as e:
        print(e)

pathWeight = twoApprox(graph_list[0])
"""
