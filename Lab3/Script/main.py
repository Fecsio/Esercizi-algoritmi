from Lab3.Script import Parser
from Lab3.Script import held_karp






graph_list = Parser.Parser()



best_sol = [35002, 3323, 21294, 426, 7013, 134602]

try:
    val, t_o, time_exec = held_karp.hk_tsp(graph_list[4], 60)
    if t_o:
        print("\nTimed out")
    print("\nSolution for graph ", graph_list[4], ": " + str(val), " time: ", round(time_exec, 2), "with error =", round((val - best_sol[4]) / best_sol[4], 2), "%")

except IOError as e:
    print(e)
