import matplotlib.pyplot as plt
from Script import DFS
from Script import Graph
from Script import Attackers
import pprint


#dato un grafo utilizza l'attacco random per ottenere le componenti x e y del grafico
def randomAttackerPlot(G):
    n = 0
    nodeNumber = G.countNodes()
    CCNumber = []
    disabledNodes = []
    while not G.isEmpty():
        n += 1
        Attackers.randomAttack(G)
        CC_afterAttack = DFS.ConnectedC(G)
        CCNumber.append(G.getMaxCC())
        disabledNodes.append(n)
        #pprint.pprint(CC_afterAttack)
    return CCNumber, disabledNodes


#dato un grafo utilizza l'attacco sui nodi di grado massimo per ottenere le componenti x e y del grafico
def maxGradeAttackerPlot(G):
    n = 0
    nodeNumber = G.countNodes()
    CCNumber = []
    disabledNodes = []
    while not G.isEmpty():
        n += 1
        Attackers.maxGradeAttack(G)
        CC_afterAttack = DFS.ConnectedC(G)
        CCNumber.append(G.getMaxCC())
        disabledNodes.append(n)
        #pprint.pprint(CC_afterAttack)
    return CCNumber, disabledNodes


def plotRandomAttack(txt, ER, UPA):
    txtCCN, txtDN = randomAttackerPlot(txt)
    erCCN, erDN = randomAttackerPlot(ER)
    upaCCN, upaDN = randomAttackerPlot(UPA)
    plt.plot(txtCCN, txtDN, label='Grafo di una rete reale')
    plt.plot(erCCN, erDN, label='Grafo creato con ER')
    plt.plot(upaCCN, upaDN, label='Grafo creato con UPA')
    plt.legend()
    plt.xlabel('numero di nodi disabilitati')
    plt.ylabel('dimensione della componente connessa più grande')
    plt.title('Test di resilienza con attacco random')
    plt.savefig("../Immagini/plot_random.png")
    plt.show()


def plotMaxGradeAttack(txt, ER, UPA):
    txtCCN, txtDN = maxGradeAttackerPlot(txt)
    erCCN, erDN = maxGradeAttackerPlot(ER)
    upaCCN, upaDN = maxGradeAttackerPlot(UPA)
    plt.plot(txtCCN, txtDN, label='Grafo di una rete reale')
    plt.plot(erCCN, erDN, label='Grafo creato con ER')
    plt.plot(upaCCN, upaDN, label='Grafo creato con UPA')
    plt.plot([0, 1], [0, 1], label='m = 2, p = 0.0006', color='w')
    plt.legend()
    plt.xlabel('numero di nodi disabilitati')
    plt.ylabel('dimensione della componente connessa più grande')
    plt.title('Test di resilienza con attacco intelligente')
    plt.savefig("../Immagini/plot_maxGrade.png")
    plt.show()
