import pprint
import time
from Lab4.Script.Parser import Parser
from Lab4.Script.kmeans import kmeans
from Lab4.Script.HierarchicalClustering import h_clustering
from Lab4.Script.ScatterPlotCluster import scatter_plot_cluster
from Lab4.Script.utils import distortion
from Lab4.Script.ScatterPlotCluster import distortionPlot

dataset_212 = Parser('unifiedCancerData_212.csv')
dataset_526 = Parser('unifiedCancerData_562.csv')
dataset_1041 = Parser('unifiedCancerData_1041.csv')
dataset_3108 = Parser('unifiedCancerData_3108.csv')
"""
# Domanda 1

start = time.time()
clusters_1 = h_clustering(dataset_3108, 15)
print("Tempo di esecuzione senza plot:", time.time()-start, "\n")

start2 = time.time()
scatter_plot_cluster(clusters_1, dataset_3108, "gerarchico_3108")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

# Domanda 2

start = time.time()
clusters_2 = kmeans(dataset_3108, 15, 5)
print("Tempo di esecuzione senza plot:", time.time()-start, '\n')

start2 = time.time()
scatter_plot_cluster(clusters_2, dataset_3108, "kmeans_3108")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

# Domanda 4

start = time.time()
clusters_4 = h_clustering(dataset_212, 9)
print("Tempo di esecuzione senza plot:", time.time()-start)

start2 = time.time()
scatter_plot_cluster(clusters_4, dataset_212, "gerarchico_212")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

# Domanda 5

start = time.time()
clusters_5 = kmeans(dataset_212, 9, 5)
print("Tempo di esecuzione senza plot:", time.time()-start)

start2 = time.time()
scatter_plot_cluster(clusters_5, dataset_212, "kmeans_212")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

#Domanda 6

clustozzo = kmeans(dataset_526, 16, 5)

clustozzo2 = h_clustering(dataset_526, 16)


print("Distorsione clustering gerarchico:", '%.5e' % distortion(clustozzo2))

print("Distorsione clustering kmeans:", '%.5e' % distortion(clustozzo))

"""

#domanda 9

kmeansDist = []
hDist = []

for clusters in range(6, 21):
    kmeansDist.append(distortion(kmeans(dataset_212, clusters, 5)))
    hDist.append(distortion(h_clustering(dataset_212, clusters)))
distortionPlot(hDist, kmeansDist, "Distorsione212", "212 Contee")


"""for clusters in range(6, 21):
    kmeansDist.append(distortion(kmeans(dataset_526, clusters, 5)))
    hDist.append(distortion(h_clustering(dataset_526, clusters)))
distortionPlot(hDist, kmeansDist, "Distorsione526", "526 Contee")"""

"""for clusters in range(6, 21):
    kmeansDist.append(distortion(kmeans(dataset_1041, clusters, 5)))
    hDist.append(distortion(h_clustering(dataset_1041, clusters)))
distortionPlot(hDist, kmeansDist, "Distorsione1041", "1041 Contee")"""


