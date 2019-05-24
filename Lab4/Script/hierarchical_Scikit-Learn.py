import pprint

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

from Lab4.Script import Parser

lists = Parser.Parser('unifiedCancerData_212.csv')
"""lists = [Contea.Contea(0, 1, 1, 0, 0), Contea.Contea(1, 3, 2.5, 0, 0), Contea.Contea(2, 1.25, 3.75, 0, 0),
        Contea.Contea(3, 7, 2, 0, 0), Contea.Contea(4, 5, 6, 0, 0), Contea.Contea(5, 6.5, 5.5, 0, 0),
       Contea.Contea(6, 6, 6, 0, 0)]"""

X = np.array([[i.x, i.y] for i in lists])

labels = [str(math.floor(i.x)) + " , " + str(math.floor(i.y)) for i in lists]

#print(labels)

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='single')

cluster.fit_predict(X)

print(cluster.labels_)



plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
plt.show()

def to_codebook(X, part):
    """
    Calculates centroids according to flat cluster assignment

    Parameters
    ----------
    X : array, (n, d)
        The n original observations with d features

    part : array, (n)
        Partition vector. p[n]=c is the cluster assigned to observation n

    Returns
    -------
    codebook : array, (k, d)
        Returns a k x d codebook with k centroids
    """
    codebook = []

    for i in range(part.min(), part.max()+1):
        codebook.append(X[part == i].mean(0))

    return np.vstack(codebook)

pprint.pprint(to_codebook(X, cluster.labels_))