import matplotlib.pyplot as plt


def TwoCurvesPrinter(title, xlabel, label1, label2, arrayY1, arrayY2, arrayX):
    plt.plot(arrayX, arrayY1, label=label1)
    plt.plot(arrayX, arrayY2, label=label2)
    plt.ylabel('Tempo Impiegato (ms)')
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend()
    plt.savefig("../" + title, bbox_inches='tight')
    plt.close()

def OneCurvePrint(title, xlabel, ylabel, arrayY, arrayX):
    plt.plot(arrayX, arrayY)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    #plt.legend()
    plt.savefig("../" + title, bbox_inches='tight')
    plt.close()



