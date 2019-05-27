import pprint
import time

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans, AgglomerativeClustering

from Lab4.Script import Parser
from Lab4.Script.kmeans import kmeans

lists = Parser.Parser('unifiedCancerData_562.csv')
"""lists = [Contea.Contea(0, 1, 1, 0, 0), Contea.Contea(1, 3, 2.5, 0, 0), Contea.Contea(2, 1.25, 3.75, 0, 0),
        Contea.Contea(3, 7, 2, 0, 0), Contea.Contea(4, 5, 6, 0, 0), Contea.Contea(5, 6.5, 5.5, 0, 0),
       Contea.Contea(6, 6, 6, 0, 0)]"""

X = np.array([[i.x, i.y] for i in lists])

labels = [str(math.floor(i.x)) + " , " + str(math.floor(i.y)) for i in lists]

#print(labels)
start=time.time()
sortedP = sorted(lists, key=lambda c: c.population, reverse=True)  # sortedP = P ordinato secondo la popolazione

init = np.array([[sortedP[i].x, sortedP[i].y] for i in range(16)], np.float)

cluster = KMeans(n_clusters=16, max_iter=5, algorithm='auto', init=init)

#cluster = AgglomerativeClustering(n_clusters=16, affinity='euclidean', linkage='single')

cluster.fit_predict(X)

print(time.time() - start)
pprint.pprint(cluster.labels_)

clustozzo2 = kmeans(lists, 16, 5)

pprint.pprint(clustozzo2.keys())
#pprint.pprint(clustozzo2)

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

    return codebook

print(to_codebook(X, cluster.labels_))