from Lab3.Script import Parser
from Lab3.Script import held_karp






graph_list = Parser.Parser()

best_sol = [35002, 3323, 21294, 426, 7013, 134602]

try:
    t_o, val, time_exec = held_karp.call_hk_tsp(1, graph_list[1])
    if t_o:
        print("\nTimed out\n")
    print("\nSolution for graph ", graph_list[1], ": " + str(val), " time: ", time_exec, "with error =", (val - best_sol[1]) / best_sol[1])

except IOError as e:
    print(e)
