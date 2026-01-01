/*
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
```

*/

function pierwszeWystapienieKlucza(lista, klucz) {
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === klucz) {
      return i;
    }
  }
  return -1;
}

// Testy

function testPierwszeWystapienieKlucza_pozytywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], -1) === 2);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 9) === 1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 2) === 0);
}

function testPierwszeWystapienieKlucza_negatywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 0) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 10) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 100) === -1);
}

function main() {
  testPierwszeWystapienieKlucza_pozytywne();
  testPierwszeWystapienieKlucza_negatywne();
}

main();

