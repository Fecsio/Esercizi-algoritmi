from Lab3.Script.Graph import Graph
from Lab3.Script.Graph import Node
from Lab3.Script.Graph import Edge
import math
import pprint
import os


def Parser():
    directory = os.fsencode('../File vari/Data')
    graphList = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        f = open('../File vari/Data/' + filename, 'r', encoding='ISO-8859-1')
        name = ""
        type = ""
        dimension = ""
        graph = None
        nodes = []
        while True:
            line = f.readline().split(':')
            if line[0].strip() == "NAME":
                name = line[1].strip("\n").strip()
            elif line[0].strip() == "EDGE_WEIGHT_TYPE":
                type = line[1].strip("\n").strip()
            elif line[0].strip() == "DIMENSION":
                dimension = line[1].strip("\n").strip()
            elif line[0].strip("\n") == "NODE_COORD_SECTION":
                break
        graph = Graph(name, type, dimension)
        for x in f:
            line = x.split()
            if line[0] == "EOF":
                break
            else:
                nodes.append(Node(line[0], (float(line[1])), (float(line[2]))))
        graph.insertNodes(nodes)
        graphList.append(graph)
    return graphList

"""g = Parser()

for gr in g:
    print(gr.type)
    for n in gr.distMatrix:
        print(n)

print(g)
list = g[1].getOrderedEdges()
for e in list:
    print(e.getWeight())"""


