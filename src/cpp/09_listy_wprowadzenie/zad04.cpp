/*
ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj `N` liczb całkowitych. Wypisz:

1. największą liczbę w liście
2. najmniejszą liczbę w liście

w jednej linii, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna linia:

* `max min`

### Przykład

**Wejście:**

```
9
4
-7
8
5
6
-9
10
2
-8
```

**Wyjście:**

```
10 -9
```

*/
#include <algorithm>
#include <cassert>
#include <limits>
#include <vector>

int maksV1(std::vector<int> &lista) {
  if (lista.empty()) return std::numeric_limits<int>::min();

  int maks = lista.front();

  for (auto liczba : lista) {
    if (liczba > maks) maks = liczba;
  }

  return maks;
}

int minV1(std::vector<int> &lista) {
  if (lista.empty()) return std::numeric_limits<int>::max();

  int min = lista.front();

  for (auto liczba : lista) {
    if (liczba < min) min = liczba;
  }

  return min;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};

  assert(maksV1(lista) == *std::max_element(lista.begin(), lista.end()));
  assert(minV1(lista) == *std::min_element(lista.begin(), lista.end()));
}

void test2() {
  std::vector<int> lista{3, -2, 4, 29, -3, -40, 8, 5, -7, -1};

  assert(maksV1(lista) == *std::max_element(lista.begin(), lista.end()));
  assert(minV1(lista) == *std::min_element(lista.begin(), lista.end()));
}

int main() {
  test1();
  test2();

  return 0;
}
