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
#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin >> n;

  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }

  int minVal = *std::min_element(lista.begin(), lista.end());
  int maxVal = *std::max_element(lista.begin(), lista.end());

  std::cout << maxVal << " " << minVal << std::endl;

  return 0;
}
