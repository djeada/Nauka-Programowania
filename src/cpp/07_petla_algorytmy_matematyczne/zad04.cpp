/*
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

*/
#include <cassert>

int silnia(int liczba) {
  int wynik = 1;

  while (liczba > 0) {
    wynik *= liczba;
    liczba--;
  }

  return wynik;
}

void testSilnia() {
  assert(silnia(0) == 1);
  assert(silnia(1) == 1);
  assert(silnia(2) == 2);
  assert(silnia(3) == 6);
  assert(silnia(4) == 24);
  assert(silnia(5) == 120);
}

int main() {
  testSilnia();

  return 0;
}
