/*
ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście

**Poziom:** ★★☆
**Tagi:** `binarne`, `rotacja`, `minimum`

### Treść

Wczytaj listę liczb całkowitych, która była posortowana rosnąco i została przesunięta w prawo o nieznaną liczbę miejsc. Znajdź indeks najmniejszego elementu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — indeks najmniejszego elementu (od `0`).

### Przykład

**Wejście:**

```
5
7
8
-1
4
5
```

**Wyjście:**

```
2
```

*/

function znajdzIndeksNajmniejszegoElementu(lista) {
  let indeksNajmniejszego = 0;

  for (let i = 1; i < lista.length; i++) {
    if (lista[i] < lista[indeksNajmniejszego]) {
      indeksNajmniejszego = i;
    }
  }

  return indeksNajmniejszego;
}

// Testy

function testZnajdzIndeksNajmniejszegoElementu() {
  console.assert(znajdzIndeksNajmniejszegoElementu([7, 8, -1, 4, 5]) === 2);
  console.assert(znajdzIndeksNajmniejszegoElementu([4, 5, 7, 8, -1]) === 4);
  console.assert(znajdzIndeksNajmniejszegoElementu([-1, 4, 5, 7, 8]) === 0);
}

testZnajdzIndeksNajmniejszegoElementu();

