/*
ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

* 1 linia: maksymalna suma klepsydry

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

*/
#include <cassert>
#include <limits>
#include <vector>

// Zlozonosc Czasowa: O(n^2)
// Zlozonosc Pamieciowa: O(1)
int klepsydraV1(std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  int wynik = __WINT_MIN__;

  int N = macierz.size();

  for (int wiersz = 0; wiersz < N; wiersz++) {
    for (int kolumna = 0; kolumna < N; kolumna++) {
      if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1))
        wynik = std::max(
            wynik,
            (macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna] +
             macierz[wiersz - 1][kolumna + 1] + macierz[wiersz][kolumna] +
             macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] +
             macierz[wiersz + 1][kolumna + 1]));
    }
  }

  return wynik;
}

void test1() {
  std::vector<std::vector<int>> macierz{{10, 99, 28, 21, 78},
                                        {35, 78, 31, 56, 24},
                                        {7, 18, 2, 50, 87},
                                        {59, 67, 9, 82, 53},
                                        {23, 26, 76, 62, 36}};

  int wynik = 395;
  assert(klepsydraV1(macierz) == wynik);
}

int main() {
  test1();
  return 0;
}
