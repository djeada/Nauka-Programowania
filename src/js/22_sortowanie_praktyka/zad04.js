/*
ZAD-04 — Sortowanie napisów według długości

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`, `list`

### Treść

Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: napis (bez spacji)

### Wyjście

* 1 linia: lista napisów posortowana jak w przykładzie

### Przykład

**Wejście:**

```
4
abcd
ab
a
abc
```

**Wyjście:**

```
['a', 'ab', 'abc', 'abcd']
```

*/

const sortowanieNapisowDlugosc = (lista) => {
  return lista.sort((a, b) => a.length - b.length);
};

// Testy
const lista1 = ["abcd", "ab", "a", "abc"];
const wynik1 = ["a", "ab", "abc", "abcd"];
const lista2 = ["kot", "pies", "zaba", "krowa"];
const wynik2 = ["kot", "pies", "zaba", "krowa"];

console.assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

