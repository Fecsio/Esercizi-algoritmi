import os
import pprint
class Node:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return self.name #+', '+self.lat+' '+self.lng #join("{}: {}".format(k, v) for k, v in self.dict.items())

    def print(self):
        print(self.name)
        print(self.lat)
        print(self.lng, '\n')


def FileParser():
    f = open('../File vari/data/bfkoord', 'r')
    dict = {}
    f.readline()
    f.readline()
    for x in f:
        smt = x.split()
        id = smt[0]
        lat = smt[1]
        lng = smt[2]
        name = ''
        if smt.__len__() == 5:
            name = smt[4].replace(',', '')
        else:
            for i in range(4,smt.__len__()):
                name = name + smt[i] + ' '
            dict[id] = Node(name, lat, lng)
    for y in dict:
        print(y)
        dict[y].print()
    f.close()

FileParser()
