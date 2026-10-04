/*
ZAD-01 — Liczby naturalne mniejsze od N

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `napisy`

### Treść

Napisz rekurencyjną funkcję `liczby_mniejsze(n)`, która zwraca napis złożony ze wszystkich liczb naturalnych mniejszych od $n$, od największej do najmniejszej, oddzielonych przecinkiem i spacją.

Program wczytuje $N$ i wypisuje wynik funkcji.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna linia: liczby `N-1, N-2, ..., 1, 0` oddzielone przecinkiem i spacją (`, `). Po ostatniej liczbie nie ma przecinka. Dla `N = 1` wynikiem jest samo `0`.

### Ograniczenia

* `1 ≤ N ≤ 100`

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
9, 8, 7, 6, 5, 4, 3, 2, 1, 0
```

Liczba `10` nie jest mniejsza od `10`, więc napis zaczyna się od `9`.

### Uwagi

* Przypadek bazowy: dla $n = 1$ jedyną mniejszą liczbą naturalną jest `0`. W kroku rekurencyjnym dopisz $n-1$ przed wynikiem wywołania dla $n-1$.

### Kod startowy

```python
def liczby_mniejsze(n):
    pass


n = int(input())
print(liczby_mniejsze(n))
```

*/

#include <cassert>
#include <string>

// Zlozonosc Czasowa: O(n^2) - kazde wywolanie skleja napisy
// Zlozonosc Pamieciowa: O(n) - przez stos rekurencji
std::string mniejszeLiczby(int n) {
  // Zwraca napis "n-1, n-2, ..., 0" (dla n >= 1).
  if (n <= 1) return "0";

  return std::to_string(n - 1) + ", " + mniejszeLiczby(n - 1);
}

void testMniejszeLiczby() {
  assert(mniejszeLiczby(1) == "0");
  assert(mniejszeLiczby(2) == "1, 0");
  assert(mniejszeLiczby(10) == "9, 8, 7, 6, 5, 4, 3, 2, 1, 0");
}

int main() {
  testMniejszeLiczby();

  return 0;
}
