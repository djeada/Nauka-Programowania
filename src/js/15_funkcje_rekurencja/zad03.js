/*
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

*/

function potega(a, b) {
  if (b === 0) {
    return 1;
  }
  return a * potega(a, b - 1);
}

function test() {
  console.assert(potega(2, 0) === 1, "Test 1 failed");
  console.assert(potega(2, 1) === 2, "Test 2 failed");
  console.assert(potega(2, 2) === 4, "Test 3 failed");
  console.assert(potega(2, 3) === 8, "Test 4 failed");
  console.assert(potega(2, 4) === 16, "Test 5 failed");
  console.assert(potega(2, 5) === 32, "Test 6 failed");
  console.assert(potega(2, 6) === 64, "Test 7 failed");
  console.assert(potega(2, 7) === 128, "Test 8 failed");
  console.assert(potega(2, 8) === 256, "Test 9 failed");
  console.assert(potega(2, 9) === 512, "Test 10 failed");
  console.assert(potega(2, 10) === 1024, "Test 11 failed");
}

test();

