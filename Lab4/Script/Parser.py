"""

codice contea, x, y, popolazione, rischio di cancro

"""
import os
from Lab4.Script import Contea

def Parser():
    directory = os.fsencode('../File vari/Data')
    dataset_list = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        f = open('../File vari/Data/' + filename, 'r', encoding='ISO-8859-1')
        dataset = list()
        for line in f:
            line = line.split(',')
            dataset.append(Contea.Contea(line[0], float(line[1]), float(line[2]),
                                      int(line[3]), float(line[4])))
        dataset_list.append(dataset)

    return dataset_list


"""
L = Parser()

for i in L:
    for j in i:
        print(j.id)
"""
