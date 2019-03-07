from Script import Node


def txtToGraph():
    f = open('as20000102.txt', 'r')
    #nodeNumber = f.readlines()[-1].split( )[0]
    myGraph = Node.Graph(0)
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    for x in f:
        myGraph.addNode(int(x.split( )[0]))
    f.close()
    r = open('as20000102.txt', 'r')
    r.readline()
    r.readline()
    r.readline()
    r.readline()
    for x in r:
        smt = x.split( )
        myGraph.addArc(int(smt[0]), int(smt[1]))
    return myGraph

