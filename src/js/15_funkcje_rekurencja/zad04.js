/*
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

*/

function silnia(n) {
  if (n === 0) {
    return 1;
  }
  return n * silnia(n - 1);
}

function test() {
  console.assert(silnia(0) === 1, "Test 1 failed");
  console.assert(silnia(1) === 1, "Test 2 failed");
  console.assert(silnia(2) === 2, "Test 3 failed");
  console.assert(silnia(3) === 6, "Test 4 failed");
  console.assert(silnia(4) === 24, "Test 5 failed");
  console.assert(silnia(5) === 120, "Test 6 failed");
  console.assert(silnia(6) === 720, "Test 7 failed");
  console.assert(silnia(7) === 5040, "Test 8 failed");
  console.assert(silnia(8) === 40320, "Test 9 failed");
  console.assert(silnia(9) === 362880, "Test 10 failed");
  console.assert(silnia(10) === 3628800, "Test 11 failed");
}

test();

