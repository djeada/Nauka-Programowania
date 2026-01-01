/*
ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy

**Poziom:** ★★★
**Tagi:** `anagram`, `zliczanie`, `greedy`

### Treść

Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.

### Wejście

* 1. linia: słowo `s1`
* 2. linia: słowo `s2`

### Wyjście

* jedna liczba całkowita: minimalna liczba usunięć lub `-1`

### Przykład

**Wejście:**

```
grazyna
razynax
```

**Wyjście:**

```
2
```

### Uwagi

* Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)

*/

// Funkcja oblicza minimalną liczbę usunięć aby uzyskać anagramy
// Złożoność czasowa: O(n), gdzie n to długość słów
// Złożoność pamięciowa: O(k), gdzie k to liczba unikalnych znaków
function minUsunieciaDoAnagramow(slowo1, slowo2) {
  if (slowo1.length !== slowo2.length) {
    return -1;
  }

  const licznik1 = {};
  const licznik2 = {};

  // Zlicz znaki w obu słowach
  for (const znak of slowo1) {
    licznik1[znak] = (licznik1[znak] || 0) + 1;
  }

  for (const znak of slowo2) {
    licznik2[znak] = (licznik2[znak] || 0) + 1;
  }

  // Oblicz różnice
  let usuniecia = 0;
  const wszystkieZnaki = new Set([
    ...Object.keys(licznik1),
    ...Object.keys(licznik2),
  ]);

  for (const znak of wszystkieZnaki) {
    const count1 = licznik1[znak] || 0;
    const count2 = licznik2[znak] || 0;
    usuniecia += Math.abs(count1 - count2);
  }

  return usuniecia;
}

// Test
function test() {
  const input1 = "grazyna";
  const input2 = "razynax";
  const expectedOutput = 2;
  const output = minUsunieciaDoAnagramow(input1, input2);

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
