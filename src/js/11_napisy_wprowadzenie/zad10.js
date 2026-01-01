/*
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

*/

function znajdzEkstremalneSlowo(napis, ekstremum) {
  let slowa = napis.split(/[^\w]+/);
  let slowoEkstremalne = slowa[0];
  for (let i = 0; i < slowa.length; i++) {
    if (slowa[i].length === ekstremum) {
      slowoEkstremalne = slowa[i];
      break;
    }
  }
  return slowoEkstremalne;
}

function znajdzNajdluzszeISkrotszeSlowo(napis) {
  let slowa = napis.split(/[^\w]+/);
  let najdluzszeSlowo = slowa[0];
  let najkrotszeSlowo = slowa[0];
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i];
    if (slowo.length > najdluzszeSlowo.length) {
      najdluzszeSlowo = slowo;
    }
    if (slowo.length < najkrotszeSlowo.length) {
      najkrotszeSlowo = slowo;
    }
  }
  najdluzszeSlowo = znajdzEkstremalneSlowo(napis, najdluzszeSlowo.length);
  najkrotszeSlowo = znajdzEkstremalneSlowo(napis, najkrotszeSlowo.length);
  return [najdluzszeSlowo, najkrotszeSlowo];
}

// Test

function test() {
  let input = "Kaczka lubi wiosne.";
  let expectedOutput = ["Kaczka", "lubi"];
  let output = znajdzNajdluzszeISkrotszeSlowo(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

