/*
ZAD-07 — Sortowanie listy 0/1/2

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1/2) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
7
1 0 1 2 2 0 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 2, 2]
```

*/

const sortuj = (lista) => {
  return lista.sort((a, b) => a - b);
};

// Testy
const lista1 = [1, 0, 1, 2, 2, 0, 1];
const wynik1 = [0, 0, 1, 1, 1, 2, 2];
const lista2 = [2, 0, 0, 1, 1, 2, 0];
const wynik2 = [0, 0, 0, 1, 1, 2, 2];

console.assert(
  JSON.stringify(sortuj(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortuj(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

