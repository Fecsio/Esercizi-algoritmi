"""

codice contea, x, y, popolazione, rischio di cancro

"""
import csv
from Lab4.Script import Contea


def Parser(filename):
    dataset = []
    with open('../File vari/Data/' + filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            dataset.append(Contea.Contea(line[0], float(line[1]), float(line[2]),
                                      int(line[3]), float(line[4])))
    return dataset



"""L = Parser('unifiedCancerData_212.csv')

for j in L:
    print(j)

"""