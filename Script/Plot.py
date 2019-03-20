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
    print(txtCCN[1294])
    print(erCCN[1294])
    print(upaCCN[1294])
    plt.plot(txtDN, txtCCN, label='Grafo di una rete reale')
    plt.plot(erDN, erCCN, label='Grafo creato con ER')
    plt.plot(upaDN, upaCCN, label='Grafo creato con UPA')
    plt.plot([0, 1], [0, 1], label='m = 2, p = 0.0006', color='w')
    plt.plot([1295, 1295], [0, 7000], color='k', linestyle=':')
    plt.plot(txtDN[1294], txtCCN[1294], 'ro', label='dimensione componente connessa più grande dopo aver rimosso il 20% dei nodi')
    plt.plot(erDN[1294], erCCN[1294], 'ro')
    plt.plot(upaDN[1294], upaCCN[1294], 'ro')
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
    plt.plot(txtDN, txtCCN, label='Grafo di una rete reale')
    plt.plot(erDN, erCCN, label='Grafo creato con ER')
    plt.plot(upaDN, upaCCN, label='Grafo creato con UPA')
    plt.plot([0, 1], [0, 1], label='m = 2, p = 0.0006', color='w')
    plt.plot([1295, 1295], [0, 7000], color='k', linestyle=':')
    plt.legend()
    plt.xlabel('numero di nodi disabilitati')
    plt.ylabel('dimensione della componente connessa più grande')
    plt.title('Test di resilienza con attacco intelligente')
    plt.savefig("../Immagini/plot_maxGrade.png")
    plt.show()
