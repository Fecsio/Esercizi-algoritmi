import os
from Lab2.Script import Nodo
import re

def FileParser():
    f = open('../File vari/data/bfkoord', 'r', encoding='ISO-8859-1')
    graph = Nodo.Graph()
    f.readline()
    f.readline()
    for x in f:
        split = x.split('%')
        name = split[1].strip('\n') #lettura nome
        smt = split[0].split() # lettura resto
        id = ''
        lng = ''
        lat = ''
        for y in smt:
            if re.match('[0-9]{9}$', y):   # controllo se è un id
                id = re.match('[0-9]{9}$', y).group(0)
            elif re.match('[0-9\.]+', y) and lng == '':  #controllo se è una longitudine
                lng = float(re.match('[0-9\.]+', y).group(0))
            elif re.match('[0-9\.]+', y):       #controllo se è un latitudine
                lat = float(re.match('[0-9\.]+', y).group(0))
        graph.addNode(id, name, lng, lat)
    f.close()
    directory = os.fsencode('../File vari/data')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith('.LIN'):
            f = open('../File vari/data/' + filename, 'r', encoding='ISO-8859-1')
            f.readline() #legge la prima riga inutile
            id = ''
            check = False  # Uso questa sentinella per capire quando una corsa sta iniziando o finendo
            #tengo le informazioni della riga precedente per poter creare l'arco, prev = [idStazionePrecedente, OrarioDiPartenza]
            prev = []
            for line in f:
                if re.match('^\*Z', line): # se la linea comincia con *Z creo l'id univoco formato da 'linea'+'corsa'
                    split = line.split()
                    id = split[2].strip('-') + split[1]
                elif re.match('\*', line): #se è una riga inutile non fare nulla
                    pass
                else:
                    info = line.split('%')[0].split()
                    idStazione = info[0]
                    partenza = 0
                    arrivo = 0
                    #viene utilizzato strip('-') perchè alcuni orari hanno un - davanti
                    # se c'è solo un orario e check è false allora abbiamo solo l'orario di partenza
                    if (not re.match('[0-9]{5}', info[info.__len__() - 2].strip('-'))) and check == False:
                        check = True
                        partenza = info[info.__len__() - 1].strip('-')
                        prev = [idStazione, partenza]
                    #se c'è solo un orario e check è true allora abbiamo solo l'orario di arrivo
                    elif (not re.match('[0-9]{5}', info[info.__len__()-2].strip('-'))) and check == True:
                        check = False
                        arrivo = info[info.__len__() - 1].strip('-')
                        graph.addEdgeTimes(prev[0], idStazione, id, prev[1], arrivo)
                    # altrimenti ho sia partenza che arrivo
                    else:
                        partenza = info[info.__len__() - 1].strip('-')
                        arrivo = info[info.__len__() - 2].strip('-')
                        graph.addEdgeTimes(prev[0], idStazione, id, prev[1], arrivo)
                        prev = [idStazione, partenza]
            f.close()
    """for e in graph.nodes:
        print(e, graph.nodes[e].nome)"""
    """for e in graph.edges:
            print(e, graph.edges[e].times)"""

    return graph


#FileParser()
