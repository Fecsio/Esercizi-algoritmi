import time
import random

from Lab3.Script import Graph


"""
Inizializzazione: considera il circuito parziale composto dal solo vertice 0. Trova un vertice j che minimizza w(0,j) e costruisci il circuito parziale (0,j);
Selezione: trova un vertice k non presente nel circuito parziale C che minimizza w(k,C) con C circuito parziale trovato finora;
Inserimento: trova un arco {i,j} del circuito parziale che minimizza il valore w(i,k) + w(k,j) - w(i,j) e inserisci k tra i e j; 
"""

def closest_selection(G, id_node, tour):
    minDist = float("inf")
    for i in range (0, G.getDim()):
        if(i != id_node and i not in tour):
            print("Nodo a: ", id_node, " Nodo b: ", i, " Distanza: ", G.getDistance(id_node, i))
            if G.getDistance(id_node, i) < minDist:
                minDist = G.getDistance(id_node, i)
                minNext = i
    return minNext

def farthest_selection(G, id_node, tour):
    maxDist = 0
    for i in range(0, G.getDim()):
        if (i != id_node and i not in tour):
            if G.getDistance(id_node, i) > maxDist:
                maxDist = G.getDistance(id_node, i)
                maxNext = i
    return maxNext

def insertion_algorithm(G):
    start = time.time()
    tour = []
    firstNode = int(random.randrange(0, G.getDim()))
    tour.append(firstNode)
    # init
    minNext = farthest_selection(G, firstNode, tour)
    print(minNext)
    tour.append(minNext)
    print("Tour: ", *tour)
    # selection
    while len(tour) < G.getDim():
        minNext = farthest_selection(G, minNext, tour)
        print("Nodo più vicino:", minNext)
        k = minNext
        # insert
        minDistance = (0, 1)
        delta_min = float("inf")
        for j in range(1, len(tour)):
            i = j - 1
            djk = G.getDistance(tour[j], k)
            print("Distanza ", tour[j], "-", k, " = ", djk)
            dik = G.getDistance(tour[i], k)
            print("Distanza ", tour[i], "-", k, " = ", dik)
            dij = G.getDistance(tour[i], tour[j])
            print("Distanza ", tour[i], "-", tour[j], " = ", dij)
            delta = djk + dik - dij
            print("Delta: ", delta, "Delta_min: ", delta_min, "MinDist:", minDistance)
            if delta < delta_min:
                minDistance = (i, j)
                delta_min = delta
        tour.insert(minDistance[1], k)
        print("Tour: ", *tour, "\n")
    lenght = 0
    for i in range(0, len(tour)-1):
        lenght += G.getDistance(tour[i], tour[i+1])
        print("Distanza", tour[i], "-", tour[i+1], "=", G.getDistance(tour[i], tour[i+1]), "--- Totale:", lenght)
    # lenght += G.getDistance(0, len(tour)-1)
    print("Lunghezza totale:", lenght)
    totTime = time.time() - start
    print("Tempo:", totTime)
    return tour, totTime