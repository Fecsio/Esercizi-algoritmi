from Script import TxtToGraph
from Script import DFS
from Script import Attackers
import pprint
"""import TxtToGraph
import DFS
import Attackers
import pprint"""

def main():
    """n_nodes = int(input("Insert desired number of nodes: "))

    p = float(input("Insert desired probability:"))

    created_graph = er_undirected(n_nodes, p)

    with open('../File vari/output.txt', 'w') as out:
        pprint.pprint(created_graph.dict, stream=out)
        out.write("\nNumero di archi = " + str(created_graph.countArcs()) + "\n")"""
    G = TxtToGraph.txtToGraph('../File vari/customInput.txt')
    pprint.pprint(G.dict)

    CC = DFS.ConnectedC(G)

    pprint.pprint(CC)

    n = 0
    """while not G.isEmpty():
        n += 1
        print(n)
        Attackers.maxGradeAttack(G)
        CC_afterAttack = DFS.ConnectedC(G)
        pprint.pprint(CC_afterAttack)"""

    while not G.isEmpty():
        n += 1
        print(n)
        Attackers.randomAttack(G)
        CC_afterAttack = DFS.ConnectedC(G)
        pprint.pprint(CC_afterAttack)


main()
