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

// Funkcja oblicza średnią długość słów w napisie
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
function sredniaDlugoscSlow(napis) {
  let slowa = napis.split(/[^\w]+/).filter(s => s.length > 0);
  
  if (slowa.length === 0) {
    return 0;
  }
  
  let sumaDlugosciSlow = 0;
  for (let i = 0; i < slowa.length; i++) {
    sumaDlugosciSlow += slowa[i].length;
  }
  
  // Dzielenie całkowite zgodnie z uwagami w zadaniu
  return Math.floor(sumaDlugosciSlow / slowa.length);
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

