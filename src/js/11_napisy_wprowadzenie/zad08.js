/*
ZAD-08 — Wypisz pionowo słowa ze zdania

**Poziom:** ★☆☆
**Tagi:** `split`, `string`

### Treść

Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.

### Wejście

* 1. linia: zdanie

### Wyjście

* wiele linii: słowa w kolejności występowania

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Ala
ma
kota
```

*/

function wypiszSlowa(napis) {
  let slowa = napis.split(/[^\w]+/);
  for (let i = 0; i < slowa.length; i++) {
    if (slowa[i] !== "") {
      console.log(slowa[i]);
    }
  }
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = ["Ala", "ma", "kota"];
  let output = [];
  console.log = function (text) {
    output.push(text);
  };
  wypiszSlowa(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

