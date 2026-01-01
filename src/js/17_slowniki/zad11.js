/*
ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość`.
a) Wypisz listę par posortowaną rosnąco po kluczach.
b) Wypisz listę par posortowaną rosnąco po wartościach.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`

### Wyjście

* 1 linia: lista par dla a)
* 2 linia: lista par dla b)

### Przykład

**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

**Wyjście:**

```
[('a', -2), ('b', 4), ('c', 3), ('x', 5)]
[('a', -2), ('c', 3), ('b', 4), ('x', 5)]
```

*/

function sortujSlownikPoKluczach(slownik) {
  const posortowaneKlucze = Object.keys(slownik).sort();
  const wynik = posortowaneKlucze.map((klucz) => [klucz, slownik[klucz]]);
  return wynik;
}

function sortujSlownikPoWartosciach(slownik) {
  const posortowaneKlucze = Object.keys(slownik).sort(
    (a, b) => slownik[a] - slownik[b]
  );
  const wynik = posortowaneKlucze.map((klucz) => [klucz, slownik[klucz]]);
  return wynik;
}

function testSortujSlownikPoKluczach() {
  const slownik = {
    c: 3,
    x: 5,
    a: -2,
    b: 4,
  };
  const wynik = sortujSlownikPoKluczach(slownik);
  const poprawnyWynik = [
    ["a", -2],
    ["b", 4],
    ["c", 3],
    ["x", 5],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiodl sie");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiodl sie");
  }
}

function testSortujSlownikPoWartosciach() {
  const slownik = {
    c: 3,
    x: 5,
    a: -2,
    b: 4,
  };
  const wynik = sortujSlownikPoWartosciach(slownik);
  const poprawnyWynik = [
    ["a", -2],
    ["c", 3],
    ["b", 4],
    ["x", 5],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiodl sie");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiodl sie");
  }
}

testSortujSlownikPoKluczach();
testSortujSlownikPoWartosciach();

