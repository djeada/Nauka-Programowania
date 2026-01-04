/*
ZAD-03 — Czy dwa słowa są anagramami?

**Poziom:** ★☆☆
**Tagi:** `anagram`, `sortowanie`, `zliczanie`

### Treść

Wczytaj dwa słowa i sprawdź, czy są anagramami (czy da się utworzyć jedno przez przestawienie liter drugiego).

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

Jedna linia:

* `Prawda` — jeśli anagramy
* `Fałsz` — jeśli nie

### Przykład

**Wejście:**

```
ula
lua
```

**Wyjście:**

```
Prawda
```

### Uwagi

* Najprościej: porównaj posortowane litery albo słowniki zliczeń znaków.

*/

function czyAnagramy(slowo1, slowo2) {
  const slowo1Male = slowo1.toLowerCase();
  const slowo2Male = slowo2.toLowerCase();

  if (slowo1Male.length !== slowo2Male.length) {
    return false;
  }

  const posortowane1 = slowo1Male.split("").sort().join("");
  const posortowane2 = slowo2Male.split("").sort().join("");

  return posortowane1 === posortowane2;
}

// Test
function test() {
  const input1 = "ula";
  const input2 = "lua";
  const expectedOutput = "Prawda";
  const wynik = czyAnagramy(input1, input2);
  const output = wynik ? "Prawda" : "Fałsz";

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to "' +
      output +
      '", a oczekiwany wynik to "' +
      expectedOutput +
      '"'
  );
  console.log("Test przeszedl pomyslnie");
}

test();
