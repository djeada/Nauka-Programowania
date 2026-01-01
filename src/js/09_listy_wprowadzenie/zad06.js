/*
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.

*/

function czySredniaWLiscie(lista) {
  let suma = 0;
  for (let i = 0; i < lista.length; i++) {
    suma += lista[i];
  }
  let srednia = suma / lista.length;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === srednia) {
      return true;
    }
  }
  return false;
}

// Testy

function testCzySredniaWLiscie_pozytywne() {
  console.assert(czySredniaWLiscie([6, 2, 1, 4, 27]) === true);
  console.assert(czySredniaWLiscie([2, 2, 2, 2, 2]) === true);
  console.assert(czySredniaWLiscie([1, 2, 3, 4, 5]) === true);
}

function testCzySredniaWLiscie_negatywne() {
  console.assert(czySredniaWLiscie([6, 2, 1, 27]) === false);
  console.assert(czySredniaWLiscie([2, 2, 2, 2]) === false);
  console.assert(czySredniaWLiscie([1, 2, 3, 4]) === false);
}

function main() {
  testCzySredniaWLiscie_pozytywne();
  testCzySredniaWLiscie_negatywne();
}

main();

