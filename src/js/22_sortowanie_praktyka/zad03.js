/*
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

* 1 linia: lista par posortowana jak w podpunkcie a)
* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

*/

const sortowanieParLiczb = (lista) => {
  return lista.sort((a, b) => a[1] - b[1]);
};

const sortowanieParDlugosciNapisow = (lista) => {
  return lista.sort((a, b) => a[0].length - b[0].length);
};

// Testy
const lista = [
  ["ab", 3],
  ["bca", 1],
  ["c", 2],
];
const wynikA = [
  ["bca", 1],
  ["c", 2],
  ["ab", 3],
];
const wynikB = [
  ["c", 2],
  ["ab", 3],
  ["bca", 1],
];

console.assert(
  JSON.stringify(sortowanieParLiczb(lista)) === JSON.stringify(wynikA),
  "Test a nieudany"
);
console.assert(
  JSON.stringify(sortowanieParDlugosciNapisow(lista)) ===
    JSON.stringify(wynikB),
  "Test b nieudany"
);

