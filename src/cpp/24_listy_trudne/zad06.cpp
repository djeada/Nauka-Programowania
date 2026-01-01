/*
ZAD-06 — Połączenie posortowanych list (unikalne)

**Poziom:** ★★★
**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz
je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez
powtórzeń**.

### Wejście

* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

*/
#include <cassert>
#include <queue>
#include <vector>

struct Wezel {
  int wartosc, i, j;
};

std::vector<int> polaczListyV1(std::vector<std::vector<int>> &lista) {
  auto cmp = [&](const Wezel &lhs, const Wezel &rhs) {
    return lhs.wartosc > rhs.wartosc;
  };

  std::priority_queue<Wezel, std::vector<Wezel>, decltype(cmp)> kolejka(cmp);
  std::vector<int> wynik;

  for (auto i = 0; i < lista.size(); i++) kolejka.push({lista[i][0], i, 0});

  while (!kolejka.empty()) {
    auto min = kolejka.top();
    kolejka.pop();

    wynik.push_back(min.wartosc);

    if (min.j + 1 < lista[min.i].size()) {
      min.j++;
      min.wartosc = lista[min.i][min.j];
      kolejka.push(min);
    }
  }

  return wynik;
}

// Testy Poprawnosc
void test1() {
  std::vector<std::vector<int>> lista{
      {-6, 23, 29, 33}, {6, 22, 35, 71}, {5, 19, 21, 37}, {-12, -7, -3, 28}};

  std::vector<int> wynik{-12, -7, -6, -3, 5,  6,  19, 21,
                         22,  23, 28, 29, 33, 35, 37, 71};

  assert(polaczListyV1(lista) == wynik);
}

void test2() {
  std::vector<std::vector<int>> lista{{1, 2, 3}, {4, 5, 6}};

  std::vector<int> wynik{1, 2, 3, 4, 5, 6};

  assert(polaczListyV1(lista) == wynik);
}

void test3() {
  std::vector<std::vector<int>> lista;
  std::vector<int> wynik;

  assert(polaczListyV1(lista) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
