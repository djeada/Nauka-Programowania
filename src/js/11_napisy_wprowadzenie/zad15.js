/*
ZAD-15 — Słowa jako lista

**Poziom:** ★☆☆
**Tagi:** `split`, `list`

### Treść

Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: lista słów (jak w przykładzie)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
["Ala", "ma", "kota"]
```

*/

function slowaZeZdania(zdanie) {
  let slowa = zdanie.split(" ");
  let wynik = [];
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i].replace(/[^\w]/g, "");
    if (slowo) {
      wynik.push(slowo);
    }
  }
  return wynik;
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = ["Ala", "ma", "kota"];
  let output = slowaZeZdania(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to [' +
      output +
      "], a oczekiwany wynik to [" +
      expectedOutput +
      "]"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

