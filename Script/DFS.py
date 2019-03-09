from Script import Graph


def ConnectedC(g):
    #color = ['white'] * g.countNodes() per usare questo bisogna fare delle modifiche agli indici perchè le liste iniziano da 0, mentre i nostri grafi da 1
    color = {}
    for n in g.dict:
        color[n] = 'white'
    CC = []
    for n in g.dict:
        if color[n] == 'white':
            comp = DFS_Visited(g, n, [], color)
            CC.append(comp)
    return CC


def DFS_Visited(g, n, visited, color):
    color[n] = 'gray'
    visited.append(n)
    adj = g.getNodeAdj(n)
    for i in adj:
        if color[i] == 'white':
            visited = DFS_Visited(g, i, visited, color)
    color[n] = 'black'
    return visited

