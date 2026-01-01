/*
ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.

### Wejście

* 1 linia: napis

### Wyjście

* Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

*/

function histogram(napis) {
  const slownik = {};
  for (let i = 0; i < napis.length; i++) {
    const znak = napis[i];
    if (slownik[znak]) {
      slownik[znak]++;
    } else {
      slownik[znak] = 1;
    }
  }
  return slownik;
}

function testHistogram() {
  const wynik1 = histogram("klasa");
  console.assert(wynik1["k"] === 1, "Test 1 nie powiodl sie");
  console.assert(wynik1["l"] === 1, "Test 2 nie powiodl sie");
  console.assert(wynik1["a"] === 2, "Test 3 nie powiodl sie");
  console.assert(wynik1["s"] === 1, "Test 4 nie powiodl sie");

  const wynik2 = histogram("ala ma kota");
  console.assert(wynik2["a"] === 4, "Test 5 nie powiodl sie");
  console.assert(wynik2["m"] === 1, "Test 6 nie powiodl sie"); // "ala ma kota" ma tylko 1 'm'
}

testHistogram();

