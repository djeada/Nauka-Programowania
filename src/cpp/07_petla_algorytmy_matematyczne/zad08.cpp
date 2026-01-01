/*
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą
pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

*/
#include <cassert>
#include <cmath>

bool pierwsza(int n) {
  if (n <= 1) return false;

  if (n % 2 == 0 && n != 2) return false;

  for (int i = 3; i <= sqrt((double)n); i += 2) {
    if (n % i == 0) return false;
  }

  return true;
}

void testPierwsza() {
  assert(pierwsza(2));
  assert(pierwsza(3));
  assert(pierwsza(5));
  assert(pierwsza(7));
  assert(pierwsza(11));
  assert(!pierwsza(14));
  assert(!pierwsza(15));
  assert(!pierwsza(16));
}

int main() {
  testPierwsza();

  return 0;
}
