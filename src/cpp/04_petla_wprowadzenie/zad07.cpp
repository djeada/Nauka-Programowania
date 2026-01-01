/*
ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik
z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po
przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz `1.00`.

*/
#include <iomanip>
#include <iostream>

int main() {
  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  int wynik = 1;
  for (unsigned int i = 0; i < n; i++) wynik *= 3.14;

  std::cout << wynik << std::endl;

  return 0;
}
