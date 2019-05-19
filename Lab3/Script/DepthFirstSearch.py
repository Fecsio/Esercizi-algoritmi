from Lab3.Script.Graph import Graph




def depthFirstSearch(graph, treeNode, orderList, parent):
    value = treeNode.getValue()
    orderList.append(value)
    pathWeight = 0
    # Partendo dal nodo selezionato come radice scorre in maniera ricorsiva l'albero
    for i in treeNode.getLinks():
        # controllo per evitare che si passi 2 volte per lo stesso nodo
        if i.getValue() != parent:
            depthFirstSearch(graph, i, orderList, value)
    # parent è -1 solo nella prima chiamata a questa funzione quindi si entrerà solamente quando tutte le chiamate
    # ricorsive sono finite e dunque la lista contenente l'ordine di scorrimento dei nodi è completa
    # quindi viene calcolato il peso del circuito
    if parent == -1:
        for i in range(len(orderList)):
            node1 = orderList[i]
            node2 = None
            if i+1 > len(orderList)-1:
                node2 = orderList[0]
            else:
                node2 = orderList[i+1]
            pathWeight += graph.getDistance(node1, node2)
        return pathWeight

