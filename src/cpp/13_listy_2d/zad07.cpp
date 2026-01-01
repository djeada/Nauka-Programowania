/*
ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała
kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* `n` wierszy zmodyfikowanej macierzy

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

*/
#include <cassert>
#include <vector>

void wyzerujV1(std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  if (macierz.empty()) return;

  int M = macierz.size();
  int N = macierz[0].size();

  int wiersze[M] = {0};
  int kolumny[N] = {0};

  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (macierz[i][j] == 0) {
        wiersze[i] = 1;
        kolumny[j] = 1;
      }
    }
  }

  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (wiersze[i] == 1 || kolumny[j] == 1) macierz[i][j] = 0;
    }
  }
}

void test1() {
  std::vector<std::vector<int>> macierz{{1, 2, 3}, {4, 0, 6}, {7, 8, 9}};

  std::vector<std::vector<int>> wynik{{1, 0, 3}, {0, 0, 0}, {7, 0, 9}};

  wyzerujV1(macierz);

  assert(macierz == wynik);
}

int main() {
  test1();
  return 0;
}
