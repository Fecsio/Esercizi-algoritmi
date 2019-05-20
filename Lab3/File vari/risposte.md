# Lab. 3 - Il Commesso Viaggiatore

***
**Componenti gruppo:**

- Federico Caldart , matricola: 1211144
- Stefano Panozzo, matricola: 1211143
- Davide Zago, matricola: 1211260

***

### Domanda 1

<table>
  <tr>
  <th></th>
  <th colspan="3">Held Karp</th>
  <th colspan="3"> Closest Insertion</th>
  <th colspan="3">2-approssimato</th>
  </tr>
  <tr>
    <th>Istanza</th>
    <th>Soluzione</th>
    <th>Tempo (s) </th>
    <th>Errore</th>
    <th>Soluzione</th>
    <th>Tempo (ms) </th>
    <th>Errore</th>
    <th>Soluzione</th>
    <th>Tempo (s) </th>
    <th>Errore</th>
  </tr>
  <tr>
     <td>burma14.tsp</td>
     <td>3323</td>
     <td>0.46</td>
     <td>0.0%</td>
     <td>3336</td>
     <td>0.1</td>
     <td>0.39%</td>
     <td>3702</td>
     <td>0.0</td>
     <td>11.41%</td>
  </tr>
  <tr>
     <td>ulysses22.tsp</td>
     <td>7105</td>
     <td>180</td>
     <td>1.31%</td>
     <td>7390</td>
     <td>0.4</td>
     <td>5.38%</td>
     <td>8363</td>
     <td>0.0</td>
     <td>19.25%</td>
  </tr>
  <tr>
     <td>eli51.tsp</td>
     <td>1011</td>
     <td>180</td>
     <td>137.32%</td>
     <td>459</td>
     <td>2.2</td>
     <td>7.75%</td>
     <td>594</td>
     <td>0.01</td>
     <td>39.44%</td>
  </tr>
  <tr>
     <td>kroD100.tsp</td>
     <td>146819</td>
     <td>180</td>
     <td>589.49%</td>
     <td>24999</td>
     <td>11.1</td>
     <td>17.39%</td>
     <td>28027</td>
     <td>0.02</td>
     <td>31.62%</td>
  </tr>
  <tr>
     <td>gr229.tsp</td>
     <td>176680</td>
     <td>180</td>
     <td>31.26%</td>
     <td>153456</td>
     <td>90.5</td>
     <td>14.01%</td>
     <td>177614</td>
     <td>0.13</td>
     <td>31.95%</td>
  </tr>
  <tr>
     <td>d493.tsp</td>
     <td>111743</td>
     <td>180</td>
     <td>219.25%</td>
     <td>41248</td>
     <td>472</td>
     <td>17.84%</td>
     <td>45190</td>
     <td>0.72</td>
     <td>29.11%</td>
  </tr>
  <tr>
     <td>dsj1000.tsp</td>
     <td>551354888</td>
     <td>180</td>
     <td>2854.79%</td>
     <td>22909568</td>
     <td>4.24e3</td>
     <td>22.78%</td>
     <td>25034577</td>
     <td>3.2</td>
     <td>34.16%</td>
  </tr>



### Domanda 2

Di seguito vengono commentati i risultati e il comportamento per ciascuno dei tre algoritmi implementati.

#### Held-Karp
Come ci si aspetta, l'algoritmo esatto Held-Karp non si comporta bene se applicato a grafi con elevato numero di nodi.
Osserviamo come in breve tempo si riesca a trovare la soluzione ottima per il grafo avente 14 nodi e in un tempo accettabile (3 minuti) si riesca ad ottenere una stima della soluzione molto vicina all'ottimo per il grafo a 22 nodi; per i successivi grafi, tuttavia, non è possibile ottenere una buona stima della soluzione in tempi brevi: anche con solamente 51 nodi, la soluzione si discosta molto dall'ottimo.
In linea generale dunque possiamo affermare che l'errore dell'algoritmo esatto aumenta con l'aumentare del numero di nodi, ma è possibile incontrare delle eccezioni; per esempio, per il grafo avente 229 nodi l'errore non è eccessivamente elevato (rimane comunque non accettabile) e ciò accade per una questione di "*fortuna*": come si può vedere dal file gr229.tsp, il grafo è composto da nodi aventi coordinate che aumentano o diminuiscono gradualmente (dunque poco distanti tra loro) e dunque, considerando che i nodi vengono visitati in un ordine non casuale, i primi circuiti trovati sono composti da archi con pesi *fortunatamente* poco elevati.

#### Closest Insertion

L'euristica costruttiva "Closest Insertion" offre un buon compromesso in termini di prestazioni e risultati ottenuti. Come si può notare, per grafi con uno scarso numero di nodi, si riesce a calcolare un percorso minimo in tempi molto brevi (<1ms) con un errore rispetto alla soluzione ottima soddisfacente. Riguardo a questo, si può notare come all'aumentare del numero di nodi l'errore sia via via crescente, fino ad arrivare al 22.78%, accettabile considerando la velocità d'esecuzione dell'algoritmo e comunque ottenendo una soluzione 2-approssimata. 
I test sono stati eseguiti scegliendo il primo nodo in maniera casuale, così da apprezzare la diversa approssimazione nei vari casi. Di seguito sono elencati i nodi di partenza con cui si sono ottenuti i risultati riportati in tabella:

<table>
  <tr>
    <th>Istanza</th>
  	<th>Nodo iniziale</th>
  </tr>
  <tr>
     <td>burma14.tsp</td>
     <td>13</td>
  </tr>
  <tr>
     <td>ulysses22.tsp</td>
     <td>10</td>
  </tr>
  <tr>
     <td>eli51.tsp</td>
     <td>12</td>
  </tr>
  <tr>
     <td>kroD100.tsp</td>
     <td>25</td>
  </tr>
  <tr>
     <td>gr229.tsp</td>
     <td>32</td>
  </tr>
  <tr>
     <td>d493.tsp</td>
     <td>377</td>
  </tr>
  <tr>
     <td>dsj1000.tsp</td>
     <td>94</td>
  </tr>
</table>



#### 2-Approssimato

Senza dubbio l'algoritmo 2-approssimato implementato creando un albero di copertura minimo con l'algoritmo di kruskal è il più efficiente.   

Questa implementazione infatti permette di trovare una soluzione approssimata in pochi secondi anche per grafi di grandi dimensioni come nel caso di dsj1000.

L'approssimazione ottenuta è abbastanza buona, dai risultati trovati si nota che l'errore relativo non dipende dalla dimensione del grafo e non supera in nessun caso il 40%, quindi la soluzione rimane sempre ben sotto al caso peggiore trovato teoricamente nel quale la soluzione approssimata è due volte superiore alla soluzione ottima.

E' possibile inoltre ottenere soluzioni migliori provando a utilizzare nodi diversi come radici dell'albero di copertura minimo, tuttavia non sembra esserci una regola per la selezione del nodo che minimizzi l'errore per ogni grafo.                                                                                                                                                                          












