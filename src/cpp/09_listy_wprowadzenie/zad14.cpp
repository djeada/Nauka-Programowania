/*
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza
jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

*/
#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int elementBezParyV1(std::vector<int> &lista) {
  std::vector<int> pom;

  for (auto liczba : lista) {
    auto i = find(pom.begin(), pom.end(), liczba);
    if (i != pom.end())
      pom.erase(i);
    else
      pom.push_back(liczba);
  }

  return pom.front();
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int elementBezParyV2(std::vector<int> &lista) {
  int wynik = 0;

  for (auto liczba : lista) wynik ^= liczba;

  return wynik;
}

void test1() {
  std::vector<int> lista{1, 3, 1, 7, 3, 1, 1};
  int wynik = 7;
  assert(elementBezParyV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 3, 1, 7, 3, 1, 1};
  int wynik = 7;
  assert(elementBezParyV2(lista) == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
