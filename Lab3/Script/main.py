from Lab3.Script.Parser import Parser
from Lab3.Script import held_karp
from Lab3.Script.twoApprox import twoApprox
import time




graph_list = Parser()
best_sol = [35002, 3323, 21294, 426, 7013, 18659688, 134602]

for i in range(0, 7):
    try:
        start = time.time()
        val = twoApprox(graph_list[i])
        """if t_o:
            print("\nTimed out")"""
        print("\nSolution for graph ", graph_list[i], ": " + str(val), " time: ", round(time.time()-start, 2), "with error =", round(100*(val - best_sol[i]) / best_sol[i], 2), "%")

    except IOError as e:
        print(e)

pathWeight = twoApprox(graph_list[0])
