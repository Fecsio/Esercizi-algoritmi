import matplotlib.pyplot as plt
import numpy as np

def scatter_plot_cluster(clusters, P):
    labels = [None for p in P]
    count = 0
    for i in clusters:
        for j in range(0, len(P)):
            if P[j] in clusters[i]:
                labels[j] = count
        count += 1

    X = np.array([[i.x, i.y] for i in P])

    img = plt.imread("../File vari/USA_Counties.png")

    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.scatter(X[:,0],X[:,1], c=labels, cmap='rainbow')

    plt.show()

