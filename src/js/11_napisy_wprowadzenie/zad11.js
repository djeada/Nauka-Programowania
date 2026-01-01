/*
ZAD-11 — Średnia długość słów

**Poziom:** ★☆☆
**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

**Wejście:**

```
Zepsuty rower.
```

**Wyjście:**

```
6
```

### Uwagi

* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

*/

function sredniaDlugoscSlow(napis) {
  let slowa = napis.split(/[^\w]+/);
  let sumaDlugosciSlow = 0;
  for (let i = 0; i < slowa.length; i++) {
    sumaDlugosciSlow += slowa[i].length;
  }
  let sredniaDlugosc = sumaDlugosciSlow / slowa.length;
  return Math.round(sredniaDlugosc);
}

// Test

function test() {
  let input = "Zepsuty rower.";
  let expectedOutput = 6;
  let output = sredniaDlugoscSlow(input);

  console.assert(
    output === expectedOutput,
    "Test nie powiodl sie dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

