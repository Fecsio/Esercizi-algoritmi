from Script import Graph
import pprint


def txtToGraph():
    # f = open('../File vari/as20000102.txt', 'r')
    f = open('../File vari/customInput.txt', 'r')
    #nodeNumber = f.readlines()[-1].split( )[0]
    myGraph = Graph.Graph(0)
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    for x in f:
        smt = x.split()
        if not myGraph.present(int(smt[0])):
            myGraph.addNode(int(smt[0]))

        if not myGraph.present(int(smt[1])):
            myGraph.addNode(int(smt[1]))

        myGraph.addArc(int(smt[0]), int(smt[1]))
    f.close()
    """r = open('../File vari/as20000102.txt', 'r')
    # r = open('../File vari/customInput.txt', 'r')
    r.readline()
    r.readline()
    r.readline()
    r.readline()
    for x in r:
        smt = x.split( )
        myGraph.addArc(int(smt[0]), int(smt[1]))"""
    return myGraph


