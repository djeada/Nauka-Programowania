/*
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi
warunkami.

*/
#include <iostream>

int main() {
  std::cout << "podaj trzy liczby:" << std::endl;

  int a;
  int b;
  int c;

  std::cin >> a;
  std::cin >> b;
  std::cin >> c;

  if (a >= b && a >= c) {
    if (b >= c)
      std::cout << c << b << a << std::endl;
    else
      std::cout << b << c << a << std::endl;
  }

  else if (c >= b && c >= a) {
    if (a >= b)
      std::cout << b << a << c << std::endl;
    else
      std::cout << a << b << c << std::endl;
  } else {
    if (a >= c)
      std::cout << c << a << b << std::endl;
    else
      std::cout << a << c << b << std::endl;
  }
  return 0;
}
