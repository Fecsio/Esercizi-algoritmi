from Script import TxtToGraph
from Script import DFS
from Script import Attackers
from Script import ER_undirected
from Script import UPA
import pprint
from Script import Plot
import sys
"""import TxtToGraph
import DFS
import Attackers
import pprint"""
sys.setrecursionlimit(7400)

def main():
    """n_nodes = int(input("Insert desired number of nodes: "))

    p = float(input("Insert desired probability:"))

    created_graph = er_undirected(n_nodes, p)

    with open('../File vari/output.txt', 'w') as out:
        pprint.pprint(created_graph.dict, stream=out)
        out.write("\nNumero di archi = " + str(created_graph.countArcs()) + "\n")"""
    #G = TxtToGraph.txtToGraph('../File vari/customInput.txt')
    #pprint.pprint(G.dict)

    #CC = DFS.ConnectedC(G)

    #pprint.pprint(CC)


    txtGraph = TxtToGraph.txtToGraph('../File vari/as20000102.txt')
    erGraph = ER_undirected.er_undirected(6474, 0.0006)
    upaGraph = UPA.UPA(6474, 2)
    """print('ER nodes:', erGraph.countNodes())
    print('ER arcs', erGraph.countArcs())
    print('UPA nodes:', upaGraph.countNodes())
    print('UPA arcs', upaGraph.countArcs())"""
    # Disegna grafico a 3 linee per l'attacco random sui 3 grafi
    Plot.plotRandomAttack(txtGraph,erGraph,upaGraph) 
    # Disegna un grafico a 3 linee dell'attacco intlligente sui 3 grafi
    Plot.plotMaxGradeAttack(txtGraph, erGraph, upaGraph)


main()
