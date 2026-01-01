/*
ZAD-01 — Odwróć napis

**Poziom:** ★☆☆
**Tagi:** `string`, `I/O`

### Treść

Wczytaj napis i wypisz go od tyłu.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: odwrócony napis

### Przykład

**Wejście:**

```
barszcz
```

**Wyjście:**

```
zczsrab
```

*/

// Funkcja odwraca kolejność znaków w napisie
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n) dla przechowania tablicy znaków i wyniku
function odwrocNapis(napis) {
  return napis.split("").reverse().join("");
}

function test() {
  let input = "barszcz";
  let expectedOutput = "zczsrab";
  let output = odwrocNapis(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

