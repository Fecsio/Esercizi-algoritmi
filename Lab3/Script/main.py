from Lab3.Script import Parser
from Lab3.Script import held_karp

graph_list = Parser.Parser()

try:
    t_o, val = held_karp.call_hk_tsp(1, graph_list[1])
    if t_o:
        print("Timed out")
    print("Solution for graph 2: " + str(val))

except IOError as e:
    print(e)
