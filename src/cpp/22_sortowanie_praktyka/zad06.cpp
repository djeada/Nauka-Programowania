/*
ZAD-06 — Sortowanie listy binarnej (0/1)

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
6
1 0 1 0 1 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 1]
```

*/

#include <algorithm>
#include <cassert>
#include <vector>

void sortuj(std::vector<int> &lista) {
  unsigned int zera = std::count(lista.begin(), lista.end(), 0);

  for (unsigned int i = 0; i < zera; i++) lista[i] = 0;

  for (unsigned int i = zera; i < lista.size(); i++) lista[i] = 1;
}

void test1() {
  std::vector<int> lista{1, 0, 0, 1, 1, 1, 0};
  std::vector<int> wynik{0, 0, 0, 1, 1, 1, 1};

  sortuj(lista);

  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{1, 1, 1, 1, 1, 1};
  std::vector<int> wynik{1, 1, 1, 1, 1, 1};

  sortuj(lista);

  assert(lista == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
