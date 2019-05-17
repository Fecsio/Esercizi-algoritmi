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
  <th colspan="3">2-approssimato</th>
  <th colspan="3"> Euristica costruttiva</th>
  </tr>
  <tr>
    <th>Istanza</th>
    <th>Soluzione</th>
    <th>Tempo (s) </th>
    <th>Errore</th>
    <th>Soluzione</th>
    <th>Tempo (s) </th>
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
     <td>3702</td>
     <td>0.0</td>
     <td>11.41%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>ulysses22.tsp</td>
     <td>7105</td>
     <td>180</td>
     <td>1.31%</td>
     <td>8363</td>
     <td>0.0</td>
     <td>19.25%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>eli51.tsp</td>
     <td>1011</td>
     <td>180</td>
     <td>137.32%</td>
     <td>594</td>
     <td>0.01</td>
     <td>39.44%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>kroD100.tsp</td>
     <td>146819</td>
     <td>180</td>
     <td>589.49%</td>
     <td>28027</td>
     <td>0.02</td>
     <td>31.62%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>gr229.tsp</td>
     <td>176680</td>
     <td>180</td>
     <td>31.26%</td>
     <td>177614</td>
     <td>0.13</td>
     <td>31.95%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>d493.tsp</td>
     <td>111743</td>
     <td>180</td>
     <td>219.25%</td>
     <td>45190</td>
     <td>0.72</td>
     <td>29.11%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  <tr>
     <td>dsj1000.tsp</td>
     <td>551354888</td>
     <td>180</td>
     <td>2854.79%</td>
     <td>25034577</td>
     <td>3.2</td>
     <td>34.16%</td>
     <td></td>
     <td></td>
     <td></td>
  </tr>
  
  
</table>

### Domanda 2

Di seguito vengono commentati i risultati e il comportamento per ciascuno dei tre algoritmi implementati.

#### Held-Karp
Come ci si aspetta, l'algoritmo esatto Held-Karp non si comporta bene se applicato a grafi con elevato numero di nodi.
Osserviamo come in breve tempo si riesca a trovare la soluzione ottima per il grafo avente 14 nodi e in un tempo accettabile (3 minuti) si riesca ad ottenere una stima della soluzione molto vicina all'ottimo per il grafo a 22 nodi; per i successivi grafi, tuttavia, non è possibile ottenere una buona stima della soluzione in tempi brevi: anche con solamente 51 nodi, la soluzione si discosta molto dall'ottimo.
In linea generale dunque possiamo affermare che l'errore dell'algoritmo esatto aumenta con l'aumentare del numero di nodi, ma è possibile incontrare delle eccezioni; per esempio, per il grafo avente 229 nodi l'errore non è eccessivamente elevato (rimane comunque non accettabile) e ciò accade per una questione di "*fortuna*": come si può vedere dal file gr229.tsp, il grafo è composto da nodi aventi coordinate che aumentano o diminuiscono gradualmente (dunque poco distanti tra loro) e dunque, considerando che i nodi vengono visitati in un ordine non casuale, i primi circuiti trovati sono composti da archi con pesi *fortunatamente* poco elevati.












