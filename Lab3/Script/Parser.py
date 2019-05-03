from Lab3.Script.Graph import Graph
from Lab3.Script.Graph import Node
import os


def Parser():
    directory = os.fsencode('../File vari/Data')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        f = open('../File vari/data/' + filename, 'r', encoding='ISO-8859-1')
        name = ""
        type = ""
        dimension = ""
        graph = None
        nodes = []
        for x in f:
            line = x.split(':')
            if line[0] == "NAME":
                name = line[1]
            elif line[0] == "TYPE":
                type = line[1]
            elif line[0] == "DIMENSION":
                dimension = line[1]
            elif line[0] == "NODE_COORD_SECTION":
                graph = Graph(name, type, dimension)
                break
        for x in f:
            if x == "EOF":
                pass
            line = x.split()
            nodes.append(Node(line[0], line[1], line[2]))
        graph.insertNodes(nodes)
        
