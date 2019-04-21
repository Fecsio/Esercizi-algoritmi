from Lab2.Script.Graph import Graph
from Lab2.Script.FileParser import FileParser
from Lab2.Script.mapPrinter import mapPrinter
from Lab2.Script.Dijkstra import DijkstraSSSP
from Lab2.Script.Time import Time
import sys
import random

def main():
    g = FileParser()
    #start = sys.argv[1]
    #destination = sys.argv[2]
    #time = sys.argv[3]
    start = random.choice(list(g.nodes))
    destination = random.choice(list(g.nodes))
    time = "02218"
    #start = input("From what node are you starting to travel? ")
    #time = input("When do you want to leave? ")
    #destination = input("Where do you want to go? ")
    try:
        t = Time(time)
        p, d, tt = DijkstraSSSP(g, start, t)
        mapPrinter(g, p, tt, destination, t.getTime())
    except AssertionError:
        print("The node does not exist")
    except IndexError:
        print("The time is wrong")


main()
