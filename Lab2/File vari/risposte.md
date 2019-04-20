# Lab 2. La rete dei trasporti pubblici

**Componenti gruppo:**

- Federico Caldart , matricola: 1211144
- Stefano Panozzo, matricola: 1211143
- Davide Zago, matricola: 1211260


***

### Domanda 1

Per modellare la rete di trasporti pubblici abbiamo utilizzato un grafo così implementato:

1. I **nodi** identificano le stazioni e hanno come campi dato il nome, le coordinate (longitudine e latitudine) e la lista degli identificativi dei nodi adiacenti; gli identificativi non sono salvati come campo dato nei nodi stessi, ma vengono utilizzati all'interno del grafo, ognuno associato ad un oggetto di classe Node.

2. Gli **archi** identificano i collegamenti tra le stazioni e hanno come campi dato i tempi di partenza e arrivo, un identificativo della corsa e un peso calcolato come differenza tra i secondi a partire dalla mezzanotte del tempo di arrivo e i secondi a partire dalla mezzanotte del tempo di partenza: tale peso non sarà negativo poichè nessun collegamento tra due stazioni parte un giorno e arriva il successivo. Gli archi non memorizzano le due stazioni collegate, che vengono invece associate a oggetti di tipo Edge all'interno del grafo.

Nella classe che modella il grafo, nodi ed archi vengono gestiti con l'ausilio di due dizionari:

1. **nodes** è un dizionario che ha come chiavi gli identificativi delle stazioni e associa ad ogni chiave un solo oggetto di tipo node, cioè una stazione.

2. **edges** è un dizionario che ha come chiavi coppie di identificativi delle stazioni (nodi), in cui il primo indica la stazione di partenza ed il secondo quella di arrivo; ad ogni chiave è associata la lista di archi (cioè oggetti di tipo edge) che collegano le due stazioni, ognuno con identificativo e orari differenti: due stazioni saranno dunque collegate da 0, 1 o più archi.





### Corse di Prova

1. Traveling form 200415016 to 200405005  
Departure time: 09:30  
Arrival time: 09:52  
09:30 : run 00360 RGTR from 200415016 to 200405026  
09:40 : run 02069 AVL from 200405026 to 200405023  
09:41 : run 02338 AVL from 200405023 to 200405005  
<img src="Immagini/200415016to200405005.png"  width="500">

2. Traveling form 300000032 to 400000122  
Departure time: 05:30  
Arrival time: 13:50  
06:26 : run 07608 C88 from 300000032 to 110501002  
06:50 : run 03781 C82 from 110501002 to 120603002  
07:01 : run 07608 C88 from 120603002 to 140307001  
07:09 : run 03781 C82 from 140307001 to 140701016  
07:16 : run 07608 C88 from 140701016 to 160904001  
07:26 : run 03781 C82 from 160904001 to 200417051  
07:39 : run 07608 C88 from 200417051 to 200405035  
07:46 : run 00055 C82 from 200405035 to 400000047  
12:07 : run 09879 C82 from 400000047 to 400000122  
<img src="Immagini/300000032to400000122.png"  width="500">

3. Traveling form 210602003 to 300000030  
Departure time: 06:30  
Arrival time: 10:53  
06:41 : run 00030 CFLBUS from 210602003 to 210202003  
06:52 : run 00032 CFLBUS from 210202003 to 210502001  
06:55 : run 00035 CFLBUS from 210502001 to 220502003  
07:06 : run 00031 CFLBUS from 220502003 to 201103004  
07:07 : run 01306 CFLBUS from 201103004 to 201103001  
07:09 : run 00022 RGTR from 201103001 to 200301002  
07:11 : run 01306 CFLBUS from 200301002 to 200301003  
07:12 : run 00035 CFLBUS from 200301003 to 200303006  
07:13 : run 00031 CFLBUS from 200303006 to 200303001  
07:14 : run 00037 CFLBUS from 200303001 to 200303007  
07:15 : run 01306 CFLBUS from 200303007 to 200304001  
07:16 : run 00035 CFLBUS from 200304001 to 200304004  
07:17 : run 00031 CFLBUS from 200304004 to 200404028  
07:19 : run 01306 CFLBUS from 200404028 to 200404016  
07:20 : run 00031 CFLBUS from 200404016 to 200405036  
07:24 : run 01173 RGTR from 200405036 to 200405026  
07:27 : run 04278 AVL from 200405026 to 200405035  
07:40 : run 07630 C82 from 200405035 to 300000030  
<img src="Immagini/210602003to300000030.png"  width="500">

4. Traveling form 200417051 to 140701016  
Departure time: 12:00  
Arrival time: 12:43  
12:20 : run 03712 C82 from 200417051 to 140701016  
<img src="Immagini/200417051to140701016.png"  width="500">

5. Traveling form 200417051 to 140701016  
Departure time: 23:55  
Arrival time: 00:44  
00:09 : run 03623 C82 from 200417051 to 140701016  
<img src="Immagini/200417051to140701016(2).png"  width="500">

