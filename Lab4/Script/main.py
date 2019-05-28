import pprint
import time
from Lab4.Script.Parser import Parser
from Lab4.Script.kmeans import kmeans
from Lab4.Script.HierarchicalClustering import h_clustering
from Lab4.Script.Plotter import scatter_plot_cluster
from Lab4.Script.utils import distortion
from Lab4.Script.Plotter import distortionPlot

dataset_212 = Parser('unifiedCancerData_212.csv')
dataset_562 = Parser('unifiedCancerData_562.csv')
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

clustozzo = kmeans(dataset_562, 16, 5)

clustozzo2 = h_clustering(dataset_562, 16)


print("Distorsione clustering gerarchico:", '%.5e' % distortion(clustozzo2))

print("Distorsione clustering kmeans:", '%.5e' % distortion(clustozzo))

"""

# Domanda 9

kmeansDist_212 = []
kmeansDist_562 = []
kmeansDist_1041 = []

hDist_212 = []
hDist_562 = []
hDist_1041 = []

h_dataset_212 = dataset_212
h_dataset_562 = dataset_562
h_dataset_1041 = dataset_1041

pre_processed = False

for k in range(6, 21):
    kmeansDist_212.append(distortion(kmeans(dataset_212, k, 5)))
    kmeansDist_562.append(distortion(kmeans(dataset_562, k, 5)))
    kmeansDist_1041.append(distortion(kmeans(dataset_1041, k, 5)))

for k in range(20, 5, -1):
    h_dataset_212 = h_clustering(h_dataset_212, k, pre_processed)
    hDist_212.append(distortion(h_dataset_212))

    h_dataset_562 = h_clustering(h_dataset_562, k, pre_processed)
    hDist_562.append(distortion(h_dataset_562))

    h_dataset_1041 = h_clustering(h_dataset_1041, k, pre_processed)
    hDist_1041.append(distortion(h_dataset_1041))

    pre_processed = True

distortionPlot(hDist_212, kmeansDist_212, "Distorsione212", "212 Contee")
distortionPlot(hDist_562, kmeansDist_562, "Distorsione562", "562 Contee")
distortionPlot(hDist_1041, kmeansDist_1041, "Distorsione1041", "1041 Contee")
