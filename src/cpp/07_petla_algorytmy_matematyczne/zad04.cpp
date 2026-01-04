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
#include <iostream>

int silnia(int n) {
  int wynik = 1;
  for (int i = 1; i <= n; i++) {
    wynik *= i;
  }
  return wynik;
}

int main() {
  int n;
  std::cin >> n;

  std::cout << silnia(n) << std::endl;

  return 0;
}
