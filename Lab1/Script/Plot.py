import matplotlib.pyplot as plt
from Lab1.Script import Attackers, DFS


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
    plt.plot([1295, 1295], [0, 7000], color='k', linestyle=':', label='20% dei nodi disabilitati')
    plt.plot(txtDN[1294], txtCCN[1294], 'ro',
             label='rete reale maxCC al 20%: ' + str(txtCCN[1294]))
    plt.plot(erDN[1294], erCCN[1294], 'bo',
             label='ER maxCC al 20%: ' + str(erCCN[1294]))
    plt.plot(upaDN[1294], upaCCN[1294], 'go',
             label='UPA macCC 20%: ' + str(upaCCN[1294]))
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
    plt.plot([1295, 1295], [0, 7000], color='k', linestyle=':', label='20% dei nodi disabilitati')
    plt.plot(txtDN[1294], txtCCN[1294], 'ro',
             label='rete reale maxCC al 20%: ' + str(txtCCN[1294]))
    plt.plot(erDN[1294], erCCN[1294], 'bo',
             label='ER maxCC al 20%: ' + str(erCCN[1294]))
    plt.plot(upaDN[1294], upaCCN[1294], 'go',
             label='UPA maxCC al 20%: ' + str(upaCCN[1294]))
    plt.legend()
    plt.xlabel('numero di nodi disabilitati')
    plt.ylabel('dimensione della componente connessa più grande')
    plt.title('Test di resilienza con attacco intelligente')
    plt.savefig("../Immagini/plot_maxGrade.png")
    plt.show()
