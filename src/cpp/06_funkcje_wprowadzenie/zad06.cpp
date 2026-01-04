/*
ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

### Wejście

Jeden argument: `n` (`n ≥ 0`)

### Wyjście

Funkcja zwraca sumę cyfr.

### Przykład

**Wywołanie funkcji:**

```python
print(suma_cyfr(13231))
```

**Wyjście:**

```
10
```

### Uwagi

* Dla `n = 0` suma cyfr to `0`.

*/
#include <iostream>

int sumaCyfr(int liczba) {
  int suma = 0;
  while (liczba > 0) {
    suma += (liczba % 10);
    liczba /= 10;
  }
  return suma;
}

int main() {
  int n;
  std::cin >> n;

  std::cout << sumaCyfr(n) << std::endl;

  return 0;
}
