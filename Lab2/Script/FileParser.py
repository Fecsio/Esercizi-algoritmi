import os
from Lab2.Script import Nodo

class Node:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return self.name

    def print(self):
        print(self.name)
        print(self.lat)
        print(self.lng, '\n')


def FileParser():
    f = open('../File vari/data/bfkoord', 'r')
    graph = Nodo.Graph()
    f.readline()
    f.readline()
    for x in f:
        smt = x.split()
        id = smt[0]
        lng = smt[1]
        lat = smt[2]
        name = ''
        if smt.__len__() == 5:
            name = smt[4].replace(',', '')
        else:
            for i in range(4, smt.__len__()):
                name = name + smt[i] + ' '
        graph.addNode(id, name, lng, lat)
    f.close()
    directory = os.fsencode('../File vari/data')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".LIN"):
            f = open('../File vari/data/' + filename, 'r')
            f.readline()
            f.close()


FileParser()
