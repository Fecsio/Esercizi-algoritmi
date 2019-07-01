# Lab. 5 -  Clustering k-means parallelo

**Componenti gruppo:**

- Federico Caldart , matricola: 1211144
- Stefano Panozzo, matricola: 1211143
- Davide Zago, matricola: 1211260
***

### Domanda 1

<img class="dist" src="Domanda 1.png"  />
<figcaption class="dist">Fig.1: Confronto tempi di calcolo seriale e parallelo al variare del numero di punti.</figcaption>

<img class="dist" src="Speedup 1.png"  />
<figcaption class="dist">Fig.1: Speedup calcolo parallelo al variare del numero di punti.</figcaption>

Lo speedup aumenta in maniera logaritmica all'aumentare del numero di punti, questo perchè il tempo di attesa dell'iterazione successiva aumenta all'aumentare del numero di punti. 

### Domanda 2

<img class="dist" src="Domanda 2.png"  />
<figcaption class="dist">Fig.2: Confronto tempi di calcolo seriale e parallelo al variare del numero di cluster.</figcaption>

<img class="dist" src="Speedup 2.png"  />
<figcaption class="dist">Fig.1: Speedup calcolo parallelo al variare del numero di cluster.</figcaption>

Lo speedup non sembra avere nessuna particolare dipendenza dal numero di cluster


### Domanda 3

<img class="dist" src="Domanda 3.png"  />
<figcaption class="dist">Fig.1: Confronto tempi di calcolo seriale e parallelo al variare del numero di iterazioni.</figcaption>

<img class="dist" src="Speedup 3.png"  />
<figcaption class="dist">Fig.1: Speedup calcolo parallelo al variare del numero di iterazioni.</figcaption>

Lo speedup sembra essere costante rispetto al numero di iterazioni, infatti il fattore rimane sempre tra 2,5 e 2, questo perché ogni iterazione dell'algoritmo parallelo fa chiamate parallele mentre ogni iterazione dell'algoritmo seriale fa le stesse chiamate ma in versione seriale, quindi la differenza tra i tempi di esecuzione aumenta in maniera lineare rispetto al numero di iterazioni.


### Domanda 4

<img class="dist" src="Domanda 4.png"  />
<figcaption class="dist">Fig.1: Confronto tempi di calcolo parallelo al variare della soglia di cutoff.</figcaption>

Il valore di cutoff che ci ha permesso di ottenere le prestazioni migliori è circa 9000, in generale vediamo che un valore di cutoff porta beneficio se non è troppo alto altrimenti la versione parallela non viene mai sfruttata, viceversa per un numero esiguo di punti non è efficiente usare l'algoritmo parallelo in quanto i costi aggiuntivi dati dalla parallelizzazione sono troppo alti rispetto al tempo effettivo di esecuzione.


### Domanda 5
#### Caratteristiche hardware

<table>
  <tr>
  <th>Processore</th>
  <td>Intel® Core™ i7-4710HQ</td>
  </tr>
  <tr>
    <th>Numero di core</th>
    <td>4 fisici * 2 virtuali</td>
  </tr>
  <tr>
    <th>Frequenza base</th>
    <td>2.5GHz</td>
  </tr>
  <tr>
    <th>Frequenza massima</th>
    <td>3.5GHz</td>
  </tr>
 </table>















