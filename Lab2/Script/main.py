from Lab2.Script.Graph import Graph
from Lab2.Script.FileParser import FileParser
from Lab2.Script.mapPrinter import mapPrinter
from Lab2.Script.Dijkstra import DijkstraSSSP
from Lab2.Script.Time import Time

def main():
    g = FileParser()
    #node = input("From what node are you starting to travel? ")
    #time = input("When do you want to leave? ")
    #destination = input("Where do you want to go? ")
    try:
        t = Time("01300")
        p, d = DijkstraSSSP(g, "500000079", t)
        mapPrinter(g, p, "300000044")
    except AssertionError:
        print("The node does not exist")
    except IndexError:
        print("The time is wrong")


main()
