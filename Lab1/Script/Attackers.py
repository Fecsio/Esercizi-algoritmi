import random


def randomAttack(graph):
    # while not graph.isEmpty():
    if not graph.isEmpty():
        n = random.choice(list(graph.getNodes()))
        graph.removeNode(n)

def maxGradeAttack(graph):
    # while not graph.isEmpty():
    if not graph.isEmpty():
        max = graph.getMaxDegreeNode()
        graph.removeNode(max)




