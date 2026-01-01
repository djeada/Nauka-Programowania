/*
ZAD-08 — Iloraz w dół bez / i %

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `odejmowanie`

### Treść

Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale
**nie używa** operatorów `/` ani `%`.

### Wejście

Dwa argumenty:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.

### Przykład

**Wywołanie funkcji:**

```python
print(zaokraglij_w_dol(7, 2))
```

**Wyjście:**

```
3
```

*/
#include <cassert>
#include <limits>

int podziel(int dzielna, int dzielnik) {
  int znak = 1;
  int licznik = 0;

  if (dzielnik == 0) return std::numeric_limits<int>::signaling_NaN();

  if (dzielna == 0) return 0;

  if (dzielna < 0) {
    znak = -1;
    dzielna = -dzielna;
  }

  if (dzielnik < 0) {
    znak *= -1;
    dzielnik = -dzielnik;
  }

  if (znak == 1) {
    licznik = 0;
    while (dzielna >= dzielnik) {
      dzielna -= dzielnik;
      licznik += 1;
    }
  }

  else {
    licznik = 1;
    while (dzielna > dzielnik) {
      dzielna -= dzielnik;
      licznik += 1;
    }
  }

  return licznik * znak;
}

void testPodziel() {
  assert(podziel(0, 1) == 0);
  assert(podziel(1, 1) == 1);
  assert(podziel(25, 5) == 5);
  assert(podziel(25, -5) == -5);
  assert(podziel(-25, 5) == -5);
  assert(podziel(-25, -5) == 5);
  assert(podziel(25, 0) == std::numeric_limits<int>::signaling_NaN());
  assert(podziel(0, 0) == std::numeric_limits<int>::signaling_NaN());
}

int main() {
  testPodziel();

  return 0;
}
