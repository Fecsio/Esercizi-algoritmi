import time
import random

from Lab3.Script import Graph


"""
Inizializzazione: considera il circuito parziale composto dal solo vertice 0. Trova un vertice j che minimizza w(0,j) e costruisci il circuito parziale (0,j);
                (si è considerato come nodo 0 il primo nodo del circuito, scelto casualmente, e non il primo nodo nel dataset; in questo modo si sono potute
                eseguire più prove e notare come il costo cambi, anche sensibilmente, in base al nodo di partenza del circuito)
Selezione: trova un vertice k non presente nel circuito parziale C che minimizza w(k,C) con C circuito parziale trovato finora;
Inserimento: trova un arco {i,j} del circuito parziale che minimizza il valore w(i,k) + w(k,j) - w(i,j) e inserisci k tra i e j; 
"""

def closest_selection(G, id_node, tour):
    minDist = float("inf")
    for i in range (0, G.getDim()):
        if(i != id_node and i not in tour):
            if G.getDistance(id_node, i) < minDist:
                minDist = G.getDistance(id_node, i)
                minNext = i
    return minNext

def insertion_algorithm(G):
    start = time.time()
    # lista di nodi (in posizione esatta) già presenti nel cirtuito parziale
    tour = []
    # selezione random del primo nodo da cui partire
    firstNode = int(random.randrange(0, G.getDim()))
    tour.append(firstNode)
    # init
    minNext = closest_selection(G, firstNode, tour)
    tour.append(minNext)
    # selection
    while len(tour) < G.getDim():
        minNext = closest_selection(G, minNext, tour)
        k = minNext
        # insert
        minDistance = (0, 1)
        delta_min = float("inf")
        for j in range(1, len(tour)):
            i = j - 1
            djk = G.getDistance(tour[j], k)
            dik = G.getDistance(tour[i], k)
            dij = G.getDistance(tour[i], tour[j])
            delta = djk + dik - dij
            if delta < delta_min:
                minDistance = (i, j)
                delta_min = delta
        tour.insert(minDistance[1], k)
    totTime = time.time() - start
    # calcolo del costo totale del circuito
    lenght = 0
    for i in range(0, len(tour)-1):
        lenght += G.getDistance(tour[i], tour[i+1])
    lenght += G.getDistance(tour[0], tour[len(tour)-1])
    return tour, totTime, lenght
