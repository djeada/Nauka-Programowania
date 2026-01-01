/*
ZAD-06 — Zamień litery „a” na „?”

**Poziom:** ★☆☆
**Tagi:** `string`, `replace`

### Treść

Wczytaj napis i zamień wszystkie wystąpienia litery `a` na znak `?`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po zamianie

### Przykład

**Wejście:**

```
Latarnik
```

**Wyjście:**

```
L?t?rnik
```

*/

// Funkcja zamienia wszystkie litery 'a' na znak '?'
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n) dla przechowania wyniku
function zamienLitery(napis) {
  return napis.replace(/a/g, "?");
}

// Testy

function test() {
  let input = "Latarnik";
  let expectedOutput = "L?t?rnik";
  let output = zamienLitery(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

