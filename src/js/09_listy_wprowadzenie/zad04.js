/*
ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj `N` liczb całkowitych. Wypisz:

1. największą liczbę w liście
2. najmniejszą liczbę w liście

w jednej linii, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna linia:

* `max min`

### Przykład

**Wejście:**

```
9
4
-7
8
5
6
-9
10
2
-8
```

**Wyjście:**

```
10 -9
```

*/

function znajdzMinMax(lista) {
  var min = lista[0];
  var max = lista[0];

  for (var i = 1; i < lista.length; i++) {
    if (lista[i] < min) {
      min = lista[i];
    }
    if (lista[i] > max) {
      max = lista[i];
    }
  }

  return [min, max];
}

// Testy

function testujZnajdzMinMax() {
  var test1 = [4, -7, 8, 5, 6, -9, 10, 2, -8];
  var wynik1 = [-9, 10];
  console.assert(
    JSON.stringify(znajdzMinMax(test1)) === JSON.stringify(wynik1)
  );

  var test2 = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  var wynik2 = [1, 1];
  console.assert(
    JSON.stringify(znajdzMinMax(test2)) === JSON.stringify(wynik2)
  );

  var test3 = [10, -10, 100, -100, 1000, -1000];
  var wynik3 = [-1000, 1000];
  console.assert(
    JSON.stringify(znajdzMinMax(test3)) === JSON.stringify(wynik3)
  );
}

testujZnajdzMinMax();

