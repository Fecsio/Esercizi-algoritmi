from Lab3.Script.Graph import Graph




"""def listToTree(edgeList):
    nodeList = []
    for e in edgeList:
        present1 = False
        present2 = False
        for i in nodeList:
            if i.getValue() == e.node1:
                present1 = True
            if i.getValue() == e.node2:
                present2 = True
        if not present1:
            nodeList.append(TreeNode())"""


def depthFirstSearch(graph, treeNode, orderList, parent):
    value = treeNode.getValue()
    orderList.append(value)
    pathWeight = 0
    for i in treeNode.getLinks():
        if i.getValue() != parent:
            depthFirstSearch(graph, i, orderList, value)
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

