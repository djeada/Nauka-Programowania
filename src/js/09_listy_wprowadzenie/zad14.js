/*
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

*/

function znajdzElementBezPary(lista) {
  let bezPary = 0;
  for (let liczba of lista) {
    bezPary ^= liczba;
  }
  return bezPary;
}

// Testy

function testZnajdzElementBezPary() {
  console.assert(znajdzElementBezPary([1, 3, 1, 7, 3, 1, 1]) === 7);
  console.assert(znajdzElementBezPary([4, 4, 2, 2, 1]) === 1);
  console.assert(znajdzElementBezPary([9, 1, 1, 8, 9, 8]) === 0);
  console.assert(znajdzElementBezPary([3, 3, 6, 6, 5, 7, 7]) === 5);
}

testZnajdzElementBezPary();

