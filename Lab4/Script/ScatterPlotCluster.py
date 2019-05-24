import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import cm


def scatter_plot_cluster(clusters, P):
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
    plt.scatter(X[:,0],X[:,1], s=3, c=labels, cmap='Dark2', alpha=0.9, edgecolors='black', linewidths=0.1)

    centers = clusters.keys()

    XC = np.array([[i[0], i[1]] for i in centers])

    plt.scatter(XC[:,0], XC[:,1], s=10, c=range(0, len(centers)), cmap='Dark2', marker='X', edgecolors='black', linewidths=0.1, zorder=2)

  #  print((X[0][0], X[0][1]))

   # plt.arrow(XC[0][0], XC[0][1], XC[1][0], XC[1][1])

    for i in range(0, len(P)):
        #plt.annotate(s='', xy=(P[i].x, P[i].y), xytext=(XC[labels[i]][0], XC[labels[i]][1]), arrowprops=dict(width=0.0001e-5, headwidth=0.0001, alpha=0.2, mutation_scale=0.1))
        plt.plot([P[i].x, XC[labels[i]][0]], [P[i].y, XC[labels[i]][1]], c=cm.get_cmap('Dark2')((labels[i])/(len(centers)-1)), lw=0.1, zorder=1)

    # plt.annotate(s='', xy=XC[:], xytext=(X[:,0], X[:,1]), arrowprops=dict(arrowstyle='->'))

    plt.savefig("../File vari/usa_", dpi=600)

