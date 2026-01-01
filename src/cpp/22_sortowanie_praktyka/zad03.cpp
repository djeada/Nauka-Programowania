/*
ZAD-03 — Sortowanie listy par względem kryterium

**Poziom:** ★☆☆
**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

* 1 linia: lista par posortowana jak w podpunkcie a)
* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

**Wejście:**

```
3
ab 3
bca 1
c 2
```

**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

*/

#include <algorithm>
#include <cassert>
#include <string>
#include <utility>
#include <vector>

void sortujWartosci(std::vector<std::pair<std::string, int>> &lista) {
  std::sort(lista.begin(), lista.end(),
            [](auto rhs, auto lhs) { return rhs.second < lhs.second; });
}

void sortujDlugosci(std::vector<std::pair<std::string, int>> &lista) {
  std::sort(lista.begin(), lista.end(), [](auto rhs, auto lhs) {
    return rhs.first.size() < lhs.first.size();
  });
}

void test1() {
  std::vector<std::pair<std::string, int>> lista{
      {"abc", 3}, {"bca", 1}, {"cab", 2}};
  std::vector<std::pair<std::string, int>> wynik{
      {"bca", 1}, {"cab", 2}, {"abc", 3}};

  sortujWartosci(lista);

  assert(lista == wynik);
}

void test2() {
  std::vector<std::pair<std::string, int>> lista{
      {"ab", 3}, {"abc", 1}, {"a", 2}};
  std::vector<std::pair<std::string, int>> wynik{
      {"a", 2}, {"ab", 3}, {"abc", 1}};

  sortujDlugosci(lista);

  assert(lista == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
