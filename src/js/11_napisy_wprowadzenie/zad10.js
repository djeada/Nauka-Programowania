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

function znajdzNajdluzszeISkrotszeSlowo(napis) {
  let slowa = napis.split(/[^\w]+/).filter(s => s.length > 0);
  
  if (slowa.length === 0) {
    return ["", ""];
  }
  
  let najdluzszeSlowo = slowa[0];
  let najkrotszeSlowo = slowa[0];
  
  for (let i = 1; i < slowa.length; i++) {
    let slowo = slowa[i];
    if (slowo.length > najdluzszeSlowo.length) {
      najdluzszeSlowo = slowo;
    }
    if (slowo.length < najkrotszeSlowo.length) {
      najkrotszeSlowo = slowo;
    }
  }
  
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

