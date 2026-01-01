/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

*/

function sumaLiczbNaturalnych(n) {
  if (n === 0) {
    return 0;
  }
  return n + sumaLiczbNaturalnych(n - 1);
}

function test() {
  console.assert(sumaLiczbNaturalnych(0) === 0, "Test 1 failed");
  console.assert(sumaLiczbNaturalnych(1) === 1, "Test 2 failed");
  console.assert(sumaLiczbNaturalnych(2) === 3, "Test 3 failed");
  console.assert(sumaLiczbNaturalnych(3) === 6, "Test 4 failed");
  console.assert(sumaLiczbNaturalnych(4) === 10, "Test 5 failed");
  console.assert(sumaLiczbNaturalnych(5) === 15, "Test 6 failed");
  console.assert(sumaLiczbNaturalnych(6) === 21, "Test 7 failed");
  console.assert(sumaLiczbNaturalnych(7) === 28, "Test 8 failed");
  console.assert(sumaLiczbNaturalnych(8) === 36, "Test 9 failed");
  console.assert(sumaLiczbNaturalnych(9) === 45, "Test 10 failed");
  console.assert(sumaLiczbNaturalnych(10) === 55, "Test 11 failed");
}

test();

