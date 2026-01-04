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
#include <cmath>
#include <iostream>

bool czy_pierwsza(int n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;

  for (int i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }

  return true;
}

int main() {
  int n;
  std::cin >> n;

  std::cout << (czy_pierwsza(n) ? "True" : "False") << std::endl;

  return 0;
}
