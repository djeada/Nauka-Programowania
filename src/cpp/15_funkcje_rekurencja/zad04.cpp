/*
ZAD-04 — Silnia

**Poziom:** ★☆☆
**Tagi:** `rekurencja`, `silnia`

### Treść

Napisz rekurencyjną funkcję `silnia(n)`, która zwraca $n! = 1 \cdot 2 \cdot \ldots \cdot n$, korzystając z zależności $0! = 1$ oraz $n! = n \cdot (n-1)!$ dla $n \ge 1$.

Program wczytuje $N$ i wypisuje $N!$.

### Wejście

Jedna liczba naturalna `N`.

### Wyjście

Jedna liczba naturalna — wartość $N!$.

### Ograniczenia

* `0 ≤ N ≤ 20`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
6
```

$3! = 3 \cdot 2 \cdot 1 = 6$.

### Kod startowy

```python
def silnia(n):
    pass


n = int(input())
print(silnia(n))
```

*/

#include <cassert>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n) - przez stos rekurencji
long long silnia(int n) {
  // Zwraca n! dla n >= 0.
  if (n == 0) return 1;

  return n * silnia(n - 1);
}

void test1() {
  assert(silnia(0) == 1);
  assert(silnia(3) == 6);
  assert(silnia(10) == 3628800);
  assert(silnia(20) == 2432902008176640000LL);
}

int main() {
  test1();

  return 0;
}
