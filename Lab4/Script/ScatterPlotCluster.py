import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import cm, colors


def scatter_plot_cluster(clusters, P, nome):
    labels = [None for p in P]
    count = 0
    size = 10000
    for i in clusters:
        for j in range(0, len(P)):
            if P[j] in clusters[i]:
                labels[j] = count
        count += 1

    X = np.array([[i.x, i.y, math.ceil(i.population/size)] for i in P])

    img = plt.imread("../File vari/USA_Counties.png")

    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.axis('off')

    cmap = colors.ListedColormap(['#DF73FF', '#7FFFD4', '#FF6600', '#708090', '#FFFFF0', '#007FFF',
                                  '#ABCDEF', '#7FFF00', '#002FA7', '#FF00FF', '#987654', '#F4C430',
                                  '#FF2400', '#177245', '#FFC0CB'])

    plt.scatter(X[:, 0], X[:, 1], s=3, c=labels, cmap=cmap, alpha=0.9, edgecolors='black', linewidths=0.1)

    centers = clusters.keys()

    XC = np.array([[i[0], i[1]] for i in centers])

    plt.scatter(XC[:, 0], XC[:, 1], s=10, c=range(0, len(centers)), cmap=cmap, marker='X', edgecolors='black',
                linewidths=0.1, zorder=3)

    for i in range(0, len(P)):
        plt.plot([P[i].x, XC[labels[i]][0]], [P[i].y, XC[labels[i]][1]],
                 c=cm.get_cmap(cmap)((labels[i])/(len(centers)-1)), lw=0.1, zorder=2)

    plt.savefig("../File vari/usa_" + nome, dpi=600, bbox_inches='tight')



def distortionPlot(heirarchical, kmeans, nome):
    dataset = [x for x in range(6, 20)]
    plt.plot(dataset, heirarchical, label='heirarchical')
    plt.plot(dataset, kmeans, label='kmeans')
    plt.xlabel('Cluster Number')
    plt.ylabel('Distortion')
    plt.title("212 Contee")
    plt.legend()
    plt.savefig("../File vari/" + nome, dpi=600, bbox_inches='tight')
