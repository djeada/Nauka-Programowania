/*
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

*/
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:"
      << std::endl;

  float suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = i / (i + 1);
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + "
               "5)/n wynosi:"
            << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = (pow(i, 2) + 5) / i;
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:"
      << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    int a = i + pow(2, i);
    suma += a;
  }

  std::cout << suma << std::endl;

  return 0;
}
