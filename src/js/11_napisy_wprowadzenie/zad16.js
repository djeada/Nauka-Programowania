/*
ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `string`, `porównanie`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach różnią się znakami.

### Wejście

* 1. linia: napis `s1`
* 2. linia: napis `s2`  (ta sama długość)

### Wyjście

* 1. linia: odległość Hamminga

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

*/

// Funkcja oblicza odległość Hamminga między dwoma napisami (liczba różniących się pozycji)
// Złożoność czasowa: O(n), gdzie n to długość napisów
// Złożoność pamięciowa: O(1)
function odlegloscHamminga(napis1, napis2) {
  let odleglosc = 0;
  for (let i = 0; i < napis1.length; i++) {
    if (napis1[i] !== napis2[i]) {
      odleglosc++;
    }
  }
  return odleglosc;
}

// Test

function test() {
  let input1 = "adam";
  let input2 = "axam";
  let expectedOutput = 1;
  let output = odlegloscHamminga(input1, input2);

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

