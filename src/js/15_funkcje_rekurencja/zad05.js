/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

*/

function fib(n) {
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

function test() {
  console.assert(fib(0) === 0, "Test 1 failed");
  console.assert(fib(1) === 1, "Test 2 failed");
  console.assert(fib(2) === 1, "Test 3 failed");
  console.assert(fib(3) === 2, "Test 4 failed");
  console.assert(fib(4) === 3, "Test 5 failed");
  console.assert(fib(5) === 5, "Test 6 failed");
  console.assert(fib(6) === 8, "Test 7 failed");
  console.assert(fib(7) === 13, "Test 8 failed");
  console.assert(fib(8) === 21, "Test 9 failed");
  console.assert(fib(9) === 34, "Test 10 failed");
  console.assert(fib(10) === 55, "Test 11 failed");
}

test();

