/*
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `delta`, `pierwiastki`, `I/O`

### Treść

Wczytaj współczynniki równania kwadratowego ( ax^2 + bx + c = 0 ). Wypisz wszystkie **rzeczywiste** miejsca zerowe w kolejności rosnącej.

### Wejście

* 1. linia: trzy liczby całkowite: `a b c` (oddzielone spacją)

### Wyjście

* Jeśli brak rzeczywistych pierwiastków: wypisz `[]`
* Jeśli jeden pierwiastek (delta = 0): wypisz go raz w formacie listy: `[x]`
* Jeśli dwa pierwiastki: wypisz w formacie listy: `[x1, x2]` gdzie `x1 ≤ x2`

**Format liczb:**

* wypisuj jako liczby zmiennoprzecinkowe (np. `-1.0`, `2.5`)

### Przykład

**Wejście:**

```
1 2 1
```

**Wyjście:**

```
[-1.0]
```

### Uwagi o formatowaniu

* Licz deltę: `Δ = b*b - 4*a*c`.
* Dla `Δ > 0`: policz oba pierwiastki i posortuj rosnąco.
* Zakładamy `a ≠ 0`.

*/

function ciag(n) {
  if (n === 1) {
    return 1;
  }
  return 1 + 2 * ciag(n - 1);
}

function test() {
  console.assert(ciag(1) === 1, "Test 1 failed");
  console.assert(ciag(2) === 3, "Test 2 failed");
  console.assert(ciag(3) === 7, "Test 3 failed");
  console.assert(ciag(4) === 15, "Test 4 failed");
  console.assert(ciag(5) === 31, "Test 5 failed");
  console.assert(ciag(6) === 63, "Test 6 failed");
  console.assert(ciag(7) === 127, "Test 7 failed");
  console.assert(ciag(8) === 255, "Test 8 failed");
  console.assert(ciag(9) === 511, "Test 9 failed");
  console.assert(ciag(10) === 1023, "Test 10 failed");
  console.assert(ciag(11) === 2047, "Test 11 failed");
}

test();

