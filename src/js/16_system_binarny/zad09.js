/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

*/

function zamienNaMaleLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 65 && kod <= 90) {
      wynik += String.fromCharCode(kod + 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

function zamienNaWielkieLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 97 && kod <= 122) {
      wynik += String.fromCharCode(kod - 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

function zamienLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 65 && kod <= 90) {
      wynik += String.fromCharCode(kod + 32);
    } else if (kod >= 97 && kod <= 122) {
      wynik += String.fromCharCode(kod - 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

// Testy

function testZamienNaMaleLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "test napisu";
  const output = zamienNaMaleLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function testZamienNaWielkieLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "TEST NAPISU";
  const output = zamienNaWielkieLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function testZamienLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "tEst NapiSU"; // Wszystkie litery odwracają wielkość
  const output = zamienLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function main() {
  testZamienNaMaleLitery();
  testZamienNaWielkieLitery();
  testZamienLitery();
}

main();

