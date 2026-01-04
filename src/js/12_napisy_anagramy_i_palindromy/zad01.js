/*
ZAD-01 — Czy słowo jest palindromem?

**Poziom:** ★☆☆
**Tagi:** `string`, `palindrom`, `I/O`

### Treść

Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).

### Wejście

* 1. linia: słowo (same litery, bez spacji)

### Wyjście

Jedna linia:

* `Prawda` — jeśli słowo jest palindromem
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
kajak
```

**Wyjście:**

```
Prawda
```

### Uwagi o formatowaniu

* Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.

*/

function czyPalindrom(slowo) {
  const slowoMale = slowo.toLowerCase();
  const odwrocone = slowoMale.split("").reverse().join("");
  return slowoMale === odwrocone;
}

// Test
function test() {
  const input = "kajak";
  const expectedOutput = "Prawda";
  const wynik = czyPalindrom(input);
  const output = wynik ? "Prawda" : "Fałsz";

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to "' +
      output +
      '", a oczekiwany wynik to "' +
      expectedOutput +
      '"'
  );
  console.log("Test przeszedl pomyslnie");
}

test();
