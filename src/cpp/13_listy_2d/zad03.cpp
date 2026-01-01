/*
ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową:
wiersz `i` to `(lista1[i], lista2[i])`. Jeśli długości są różne, wypisz: `Pusta
macierz`

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Jeśli `n = m`: `n` wierszy `x y`
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::pair<int, int>> macierz(std::vector<int> listaA,
                                         std::vector<int> listaB) {
  /**
   *
   */
  std::vector<std::pair<int, int>> macierz;

  if (listaA.size() != listaB.size()) return macierz;

  int n = listaA.size();
  macierz.reserve(n);

  for (int i = 0; i < n; i++)
    macierz.push_back(std::pair<int, int>(listaA[i], listaB[i]));

  return macierz;
}

void test1() {
  std::vector<std::pair<int, int>> wynik{{3, 2}, {5, 8}, {2, 1}};
  std::vector<int> listaA{3, 5, 2};
  std::vector<int> listaB{2, 8, 1};
  assert(macierz(listaA, listaB) == wynik);
}

int main() {
  test1();
  return 0;
}
