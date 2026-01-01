/*
ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem
wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `n` wierszy obróconej macierzy

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

*/
#include <cassert>
#include <vector>

void obroc(std::vector<std::vector<int>> &macierz) {
  /**
   * Funkcja obraca macierz o 90 stopni
   */

  int N = macierz.size();

  for (int i = 0; i < N / 2; i++) {
    int pierwszy = i + 1;
    int ostatni = N - 1 - i;

    for (int j = pierwszy; j < ostatni; j++) {
      int pom = macierz[i][j];
      macierz[i][j] = macierz[N - 1 - j][i];
      macierz[N - 1 - j][i] = macierz[N - 1 - i][N - 1 - j];
      macierz[N - 1 - i][N - 1 - j] = macierz[j][N - 1 - i];
      macierz[j][N - 1 - i] = pom;
    }

    int pom = macierz[i][i];
    macierz[i][i] = macierz[N - 1 - i][i];
    macierz[N - 1 - i][i] = macierz[N - 1 - i][N - 1 - i];
    macierz[N - 1 - i][N - 1 - i] = macierz[i][N - 1 - i];
    macierz[i][N - 1 - i] = pom;
  }
}

void testObroc() {
  std::vector<std::vector<int>> macierz{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  std::vector<std::vector<int>> wynik{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}};

  obroc(macierz);
  assert(macierz == wynik);
}

int main() {
  testObroc();

  return 0;
}
