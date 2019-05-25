import time
from Lab4.Script.Parser import Parser
from Lab4.Script.kmeans import kmeans
from Lab4.Script.ScatterPlotCluster import scatter_plot_cluster
import pprint

dataset_212 = Parser('unifiedCancerData_212.csv')
dataset_526 = Parser('unifiedCancerData_562.csv')
dataset_1041 = Parser('unifiedCancerData_1041.csv')
dataset_3108 = Parser('unifiedCancerData_3108.csv')

print("Kmeans:")
start = time.time()
clusters = kmeans(dataset_3108, 15, 100)
print(time.time()-start)

scatter_plot_cluster(clusters, dataset_3108, "kmeans_3108")
pprint.pprint(clusters.keys())

