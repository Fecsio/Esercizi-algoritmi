import time
from Lab4.Script.Parser import Parser
from Lab4.Script.kmeans import kmeans
from Lab4.Script.HierarchicalClustering import h_clustering
from Lab4.Script.ScatterPlotCluster import scatter_plot_cluster

dataset_212 = Parser('unifiedCancerData_212.csv')
dataset_526 = Parser('unifiedCancerData_562.csv')
dataset_1041 = Parser('unifiedCancerData_1041.csv')
dataset_3108 = Parser('unifiedCancerData_3108.csv')

# Domanda 1

start = time.time()
clusters = h_clustering(dataset_3108, 15)
print("Tempo di esecuzione senza plot:", time.time()-start, "\n")

start2 = time.time()
scatter_plot_cluster(clusters, dataset_3108, "gerarchico_3108")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

# Domanda 2

start = time.time()
clusters = kmeans(dataset_3108, 15, 5)
print("Tempo di esecuzione senza plot:", time.time()-start, '\n')

start2 = time.time()
scatter_plot_cluster(clusters, dataset_3108, "kmeans_3108")
print("Tempo di esecuzione plot:", time.time()-start2, '\n')

# Domanda 4

start = time.time()
clusters = h_clustering(dataset_212, 9)
print("Tempo di esecuzione senza plot:", time.time()-start)

start2 = time.time()
scatter_plot_cluster(clusters, dataset_212, "gerarchico_212", '\n')
print("Tempo di esecuzione plot:", time.time()-start2)

# Domanda 5

start = time.time()
clusters = kmeans(dataset_212, 9, 5)
print("Tempo di esecuzione senza plot:", time.time()-start)

start2 = time.time()
scatter_plot_cluster(clusters, dataset_212, "kmeans_212", '\n')
print("Tempo di esecuzione plot:", time.time()-start2)

