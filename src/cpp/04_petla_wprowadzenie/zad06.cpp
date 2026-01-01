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
#include <iostream>

int main() {
  int n;
  std::cin >> n;

  // a) suma k^2 + k + 1 dla k=1..n
  int suma_a = 0;
  for (int k = 1; k <= n; k++) {
    suma_a += k * k + k + 1;
  }
  std::cout << suma_a << std::endl;

  // b) suma k^2 + 5k dla k=1..n
  int suma_b = 0;
  for (int k = 1; k <= n; k++) {
    suma_b += k * k + 5 * k;
  }
  std::cout << suma_b << std::endl;

  // c) suma k + 2k = 3k dla k=1..n
  int suma_c = 0;
  for (int k = 1; k <= n; k++) {
    suma_c += 3 * k;
  }
  std::cout << suma_c << std::endl;

  return 0;
}
