/*
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca
cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

*/
#include <cmath>
#include <iostream>

bool pierwszaWieksza(int a, int b) { return a > b; }

bool sumaMniejsza10(int a, int b) { return a + b < 10; }

bool obieNieparzyste(int a, int b) { return a % 2 == 1 && b % 2 == 1; }

int wieksza(int a, int b) { return a > b ? a : b; }

bool wiekszaMniejszaPierwszaKwadrat(int a, int b) {
  return wieksza(a, b) < a * a;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  std::cout << (pierwszaWieksza(a, b) ? "True" : "False") << std::endl;
  std::cout << (sumaMniejsza10(a, b) ? "True" : "False") << std::endl;
  std::cout << (obieNieparzyste(a, b) ? "True" : "False") << std::endl;
  std::cout << (wiekszaMniejszaPierwszaKwadrat(a, b) ? "True" : "False")
            << std::endl;

  return 0;
}
