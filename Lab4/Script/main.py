import time
from Lab4.Script import Parser
from Lab4.Script.kmeans import kmeans
from Lab4.Script.kmeans_2 import kmeans as kmeans_2
from Lab4.Script.kmeans_3 import kmeans as kmeans_3

dataset_212 = Parser.Parser('unifiedCancerData_212.csv')
dataset_526 = Parser.Parser('unifiedCancerData_562.csv')
dataset_1041 = Parser.Parser('unifiedCancerData_1041.csv')
dataset_3108 = Parser.Parser('unifiedCancerData_3108.csv')

print("Kmeans:")
start=time.time()
clusters = kmeans(dataset_3108, 100, 300)
print(time.time()-start)

print("Kmeans_2:")
start=time.time()
clusters = kmeans_2(dataset_3108, 100, 300)
print(time.time()-start)

print("Kmeans_3:")
start=time.time()
clusters = kmeans_3(dataset_3108, 100, 300)
print(time.time()-start)



