/*
ZAD-06 — Połączenie posortowanych list (unikalne)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.

### Wejście

* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

*/

const polaczListy = (lista) => {
  let result = [];
  for (let i = 0; i < lista.length; i++) {
    result = result.concat(lista[i]);
  }
  return result.sort((a, b) => a - b);
};

// Testy
const lista1 = [
  [-6, 23, 29, 33],
  [6, 22, 35, 71],
  [5, 19, 21, 37],
  [-12, -7, -3, 28],
];
const wynik1 = [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71];
const lista2 = [
  [-6, 23, 29, 33],
  [6, 22, 35, 71],
  [5, 19, 21, 37],
  [-12, -7, -3, 28],
  [0, 1, 2, 3],
];
const wynik2 = [
  -12, -7, -6, -3, 0, 1, 2, 3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71,
];

console.assert(
  JSON.stringify(polaczListy(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(polaczListy(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

