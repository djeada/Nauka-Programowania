/*
ZAD-08 — Najbliższa potęga dwójki (>= n)

**Poziom:** ★☆☆
**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsze `2^k ≥ n`.

### Przykład

**Wejście:**

```
111
```

**Wyjście:**

```
128
```

### Uwagi

* Dla `n = 0` przyjmij wynik `1`.

*/

function najblizszaPotegaDwojki(n) {
  let potegaDwojki = 1;
  while (potegaDwojki < n) {
    potegaDwojki *= 2;
  }
  return potegaDwojki;
}

// Testy
function test() {
  const input = 111;
  const expectedOutput = 128;
  const output = najblizszaPotegaDwojki(input);
  console.assert(
    output === expectedOutput,
    "Dla ${input} otrzymano ${output}, oczekiwano ${expectedOutput}"
  );
  console.log("Test passed!");
}

test();

