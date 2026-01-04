/*
ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb
naturalnych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

**Wyjście:**

```
15
```

*/
#include <iostream>

int nwd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  std::cout << nwd(a, b) << std::endl;

  return 0;
}
