/*
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej**
pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

*/
#include <algorithm>
#include <cassert>
#include <vector>

std::vector<std::pair<int, int>> znajdzParyV1(std::vector<int> &lista,
                                              int suma) {
  std::vector<std::pair<int, int>> wynik;

  for (unsigned int i = 0; i < lista.size(); i++) {
    for (unsigned int j = i + 1; j < lista.size(); j++) {
      if (lista[i] + lista[j] == suma) wynik.emplace_back(lista[i], lista[j]);
    }
  }

  return wynik;
}

void test1() {
  std::vector<int> lista{0, 4, 5, 6, 2, 9, 2, 3};
  std::vector<std::pair<int, int>> wynik{{0, 5}, {2, 3}, {2, 3}};
  int suma = 5;

  assert(znajdzParyV1(lista, suma) == wynik);
}

int main() {
  test1();

  return 0;
}
