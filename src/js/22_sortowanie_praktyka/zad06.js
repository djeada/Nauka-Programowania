/*
ZAD-06 — Sortowanie listy binarnej (0/1)

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
6
1 0 1 0 1 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 1]
```

*/

const sortowanieListyBinarnej = (lista) => {
  return lista.sort((a, b) => a - b);
};

// Testy
const lista1 = [1, 0, 1, 0, 1, 1];
const wynik1 = [0, 0, 1, 1, 1, 1];
const lista2 = [1, 1, 0, 0, 1, 0];
const wynik2 = [0, 0, 0, 1, 1, 1];

console.assert(
  JSON.stringify(sortowanieListyBinarnej(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieListyBinarnej(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

