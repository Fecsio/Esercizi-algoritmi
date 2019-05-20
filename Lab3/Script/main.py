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

for j in range(0, 7):
    minTime = 0
    minLength = float("inf")
    minTour = []
    for i in range(0,100):
        tour, time, Length = ch.insertion_algorithm(graph_list[j])
        if(Length < minLength):
            minLength = Length
            minTime = time
            minTour = tour
    print("\nSolution for graph ", graph_list[j], "First node:", tour[0], "Length:", minLength, "Time:", round(1000*minTime, 6), "with error =", round(100*(minLength - best_sol[j]) / best_sol[j], 2), "%")

"""
for i in range(0, 7):
    try:
        start = time.time()
        val = twoApprox(graph_list[i])
        print("\nSolution for graph ", graph_list[i], ": " + str(val), " time: ", round(1000*(time.time()-start), 6), "with error =", round(100*(val - best_sol[i]) / best_sol[i], 2), "%")

    except IOError as e:
        print(e)

for i in range(0,7)
    try:
        val, t_o, time_exec = held_karp.hk_tsp(graph_list[i], 180)
        if t_o:
            print("\nTimed out")
        print("\nSolution for graph ", graph_list[i], ": " + str(val), " time: ", round(time_exec, 2), "with error =", round((val - best_sol[i]) / best_sol[i], 2), "%")

    except IOError as e:
        print(e)
    
"""