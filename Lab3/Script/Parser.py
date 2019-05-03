from Lab3.Script.Graph import Graph
from Lab3.Script.Graph import Node
import os


def Parser():
    directory = os.fsencode('../File vari/Data')
    graph = None
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("eil51.tsp"):
            f = open('../File vari/data/' + filename, 'r', encoding='ISO-8859-1')
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
                elif line[0] == "NODE_COORD_SECTION":
                    break
            graph = Graph(name, type, dimension)
            for x in f:
                if x == "EOF":
                    pass
                line = x.split()
                nodes.append(Node(line[0], line[1], line[2]))
            graph.insertNodes(nodes)
    return graph

g = Parser()
print(g.type)
print("xD", g.distMatrix)
