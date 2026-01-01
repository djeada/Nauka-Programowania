/*
ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz elementy, które występują **tylko
w jednej** z list (różnica symetryczna).

* Kolejność elementów w wyniku może być **dowolna**.
* Jeśli wszystkie elementy są wspólne — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów niewspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście (jedna z poprawnych odpowiedzi):**

```
[9, 5, 1]
```

*/
#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

// Zlozonosc obliczeniowa O(n^2)
// Zlozonosc pamieciowa O(n)
std::vector<int> roznicaV1(std::vector<int> &listaA, std::vector<int> &listaB) {
  std::vector<int> wynik;

  for (auto liczba : listaA) {
    if (find(listaB.begin(), listaB.end(), liczba) == listaB.end())
      wynik.push_back(liczba);
  }

  for (auto liczba : listaB) {
    if (find(listaA.begin(), listaA.end(), liczba) == listaA.end())
      wynik.push_back(liczba);
  }

  return wynik;
}

// Zlozonosc obliczeniowa O(nlogn)
// Zlozonosc pamieciowa O(n)
std::vector<int> roznicaV2(std::vector<int> &listaA, std::vector<int> &listaB) {
  std::vector<int> wynik;
  sort(listaA.begin(), listaA.end());
  sort(listaB.begin(), listaB.end());
  set_difference(listaA.begin(), listaA.end(), listaB.begin(), listaB.end(),
                 inserter(wynik, wynik.begin()));
  set_difference(listaB.begin(), listaB.end(), listaA.begin(), listaA.end(),
                 inserter(wynik, wynik.begin()));

  return wynik;
}

bool wektoryRowne(std::vector<int> v1, std::vector<int> v2) {
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  return v1 == v2;
}

void test1() {
  std::vector<int> listaA{9, 2, 5, 4};
  std::vector<int> listaB{4, 2, 1};
  std::vector<int> wynik{9, 5, 1};
  assert(wektoryRowne(roznicaV1(listaA, listaB), wynik));
}

void test2() {
  std::vector<int> listaA{9, 2, 5, 4};
  std::vector<int> listaB{4, 2, 1};
  std::vector<int> wynik{9, 5, 1};
  assert(wektoryRowne(roznicaV2(listaA, listaB), wynik));
}

int main() {
  test1();
  test2();

  return 0;
}
