/*
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez
operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

*/
#include <cassert>
#include <cmath>

double potega(int podstawa, int wykladnik) {
  int wynik = 1;
  for (int i = 0; i < abs(wykladnik); i++) wynik *= podstawa;

  if (wykladnik < 0) return 1 / wynik;

  return wynik;
}

void testPotega() {
  assert(potega(2, 3) == 8);
  assert(potega(2, -3) == 0.125);
}

int main() {
  testPotega();

  return 0;
}
