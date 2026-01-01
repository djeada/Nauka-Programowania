/*
ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po konwersji

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

*/

// Funkcja zamienia wszystkie małe litery na wielkie
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n) dla przechowania wyniku
function zamienNaDuze(napis) {
  return napis.toUpperCase();
}

// Testy

function test() {
  let input = "Rumcajs";
  let expectedOutput = "RUMCAJS";
  let output = zamienNaDuze(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

