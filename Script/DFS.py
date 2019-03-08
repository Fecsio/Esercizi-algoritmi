from Script import Graph


def DFS(g):
    color = []
    for n in g:
        color[n] = 'white'
    CC = []
    for n in g:
        if color[n] == 'white':
            comp = DFS_Visited(g,n,[],color)
            CC  = Union(CC,comp)


def DFS_Visited(g,n,v,color):
    color[n] = 'gray'
    v.append(n)
    adj = g.getNodeAdj(n)
    for i in adj:
        if color[i] == 'white':
            v = DFS_Visited(g,i,v,color)
    color[n] = 'black'
    return v

