/*
ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od
0) ma wartość `i*j`.

### Wejście

* 1. linia: `n`

### Wyjście

* `n` wierszy po `n` liczb

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::vector<int>> macierz(int n) {
  /**
   *
   */
  std::vector<std::vector<int>> macierz;
  macierz.reserve(n);

  for (int i = 0; i < n; i++) {
    std::vector<int> wiersz;
    for (int j = 0; j < n; j++) wiersz.push_back(i * j);
    macierz.push_back(wiersz);
  }

  return macierz;
}

void test1() {
  int n = 4;
  std::vector<std::vector<int>> wynik{
      {0, 0, 0, 0}, {0, 1, 2, 3}, {0, 2, 4, 6}, {0, 3, 6, 9}};
  assert(macierz(n) == wynik);
}

int main() {
  test1();
  return 0;
}
