from Lab3.Script.Graph import Graph
from Lab3.Script.Graph import Node
import pprint
import os


def Parser():
    directory = os.fsencode('../File vari/Data')
    graph = None
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("eil51.tsp"):
            f = open('../File vari/Data/' + filename, 'r', encoding='ISO-8859-1')
            name = ""
            type = ""
            dimension = ""

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
                    pass
                else:
                    nodes.append(Node(line[0], int(line[1]), int(line[2])))
            graph.insertNodes(nodes)
    return graph

g = Parser()
print(g.type)
for x in g.distMatrix:
    print(x)