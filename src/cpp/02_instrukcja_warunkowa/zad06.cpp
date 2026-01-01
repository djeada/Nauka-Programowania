/*
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

*/
#include <iostream>

int main() {
  std::cout << "podaj cztery liczby:" << std::endl;

  int a;
  int b;
  int c;
  int d;

  std::cin >> a;
  std::cin >> b;
  std::cin >> c;
  std::cin >> d;

  int maksAB = a > b ? a : b;
  int maksCD = c > d ? c : d;
  int maks = maksAB > maksCD ? maksAB : maksCD;

  std::cout << maks << std::endl;

  return 0;
}
