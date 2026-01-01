/*
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

*/

function zamienNaKodyASCII(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    wynik += napis.charCodeAt(i);
    if (i !== napis.length - 1) {
      wynik += ", ";
    }
  }
  return wynik;
}

// Testy

function test() {
  let input = "Robot";
  let expectedOutput = "82, 111, 98, 111, 116";
  let output = zamienNaKodyASCII(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

