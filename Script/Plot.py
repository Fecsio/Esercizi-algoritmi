import matplotlib.pyplot as plt
from Script import DFS
from Script import Graph
from Script import Attackers
import pprint

# Dato il grafo effettua l'attacco randomico e disegna il grafico
def randomAttackerPlot(G):
    n = 0
    nodeNumber = G.countNodes()
    CCNumber = []
    disabledNodes = []
    while not G.isEmpty():
        n += 1
        print(n)
        Attackers.randomAttack(G)
        CC_afterAttack = DFS.ConnectedC(G)
        CCNumber.append(G.getMaxCC())
        disabledNodes.append(n)
        pprint.pprint(CC_afterAttack)
        print('resilience: ', G.getResilience(nodeNumber))
    plt.plot(disabledNodes, CCNumber)
    plt.xlabel('numero di nodi disabilitati')
    plt.ylabel('dimensione della componente connessa più grande')
    plt.title('Test di resilienza con attacco random')
    plt.show()
