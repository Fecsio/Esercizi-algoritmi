from Lab3.Script import Parser
from Lab3.Script import held_karp






graph_list = Parser.Parser()

best_sol = [35002, 3323, 21294, 426, 7013, 18659688, 134602]

for i in range(0, 7):
    try:
        val, t_o, time_exec = held_karp.hk_tsp(graph_list[i], 180)
        if t_o:
            print("\nTimed out")
        print("\nSolution for graph ", graph_list[i], ": " + str(val), " time: ", round(time_exec, 2), "with error =", round(100*(val - best_sol[i]) / best_sol[i], 2), "%")

    except IOError as e:
        print(e)
