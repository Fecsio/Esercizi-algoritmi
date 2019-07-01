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

def OneCurvePrint(title, xlabel, ylabel, arrayY, arrayX, add = False):
    if(add):
        plt.plot(arrayX, arrayY, label='Parallelo con cutoff')
        plt.plot(arrayX, [10273] * len(arrayX), label = 'Parallelo senza cutoff', linestyle='--')
        my_xticks = [10] + list(range(5000, 40000, 5000))
        plt.xticks(my_xticks)
    if(add == False):
        plt.plot(arrayX, arrayY, label='Speedup')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend()
    plt.savefig("../" + title, bbox_inches='tight')
    plt.close()



