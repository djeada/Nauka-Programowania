/*
ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości**
`(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w
osobnej linii jako: `a b`

Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Wiele linii — po jednej parze na linię.
Jeśli brak par — brak wyjścia.

### Przykład

**Wejście:**

```
5
1
2
4
3
7
5
```

**Wyjście:**

```
1 4
2 3
```

*/
#include <algorithm>
#include <cassert>
#include <vector>

std::pair<int, int> sumaDwochV1(std::vector<int> &lista, int liczba) {
  int n = lista.size();

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (lista[j] + lista[i] == liczba) return std::pair<int, int>(i, j);
    }
  }

  return std::pair<int, int>(-1, -1);
}

void test1() {
  std::vector<int> lista{1, 3, 4, 5, 2};
  int liczba = 5;
  std::pair<int, int> wynik(0, 2);
  assert(sumaDwochV1(lista, liczba) == wynik);
}

void test2() {
  std::vector<int> lista{2, -6, 10, 21, 8};
  int liczba = 7;
  std::pair<int, int> wynik(-1, -1);
  assert(sumaDwochV1(lista, liczba) == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
