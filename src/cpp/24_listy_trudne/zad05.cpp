/*
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj
zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona
opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli
chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <set>
#include <vector>

// Zlozonosc czasowa O(n.2^n)
// Zlozonosc pamieciowa O(n)
std::set<std::vector<int>> zbiorPotegowy(std::vector<int> lista) {
  sort(lista.begin(), lista.end());

  int N = pow(2, lista.size());
  std::set<std::vector<int>> zbiorPotegowy;

  for (auto i = 0; i < N; i++) {
    std::vector<int> podzbior;

    for (auto j = 0; j < lista.size(); j++) {
      if (i & (1 << j)) podzbior.push_back(lista[j]);
    }

    zbiorPotegowy.insert(podzbior);
  }

  return zbiorPotegowy;
}

// Testy Poprawnosc
void test1() {
  std::vector<int> lista{1, 2, 1};
  std::set<std::vector<int>> wynik{
      std::vector<int>({1, 2}), std::vector<int>({1}),
      std::vector<int>({2}),    std::vector<int>({1, 1, 2}),
      std::vector<int>({}),     std::vector<int>({1, 1})};

  assert(zbiorPotegowy(lista) == wynik);
}

void test2() {
  std::vector<int> lista{5, 3};
  std::set<std::vector<int>> wynik{std::vector<int>({3}),
                                   std::vector<int>({3, 5}),
                                   std::vector<int>({5}), std::vector<int>({})};

  assert(zbiorPotegowy(lista) == wynik);
}

void test3() {
  std::vector<int> lista;
  std::set<std::vector<int>> wynik{std::vector<int>({})};

  assert(zbiorPotegowy(lista) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
