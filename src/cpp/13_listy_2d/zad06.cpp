/*
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na
siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

*/
#include <algorithm>
#include <cassert>
#include <utility>
#include <vector>

// Zlozonosc Czasowa: O(n log n)
// Zlozonosc Pamieciowa: O(n)
std::vector<std::pair<int, int>> polaczPrzedzialyV1(
    std::vector<std::pair<int, int>> &lista) {
  /**
   *
   */
  sort(lista.begin(), lista.end());

  int pocz = lista.front().first;
  int koniec = lista.front().second;
  lista.erase(lista.begin());

  std::vector<std::pair<int, int>> wynik;

  for (const auto &para : lista) {
    if (koniec >= para.first) {
      if (koniec < para.second) koniec = para.second;
    } else {
      wynik.push_back(std::pair<int, int>(pocz, koniec));
      pocz = para.first;
      koniec = para.second;
    }
  }

  wynik.push_back(std::pair<int, int>(pocz, koniec));

  return wynik;
}

void test1() {
  std::vector<std::pair<int, int>> lista{{23, 67}, {23, 53}, {45, 88}, {77, 88},
                                         {10, 22}, {11, 12}, {42, 45}};

  std::vector<std::pair<int, int>> wynik{{10, 22}, {23, 88}};
  assert(polaczPrzedzialyV1(lista) == wynik);
}

int main() {
  test1();
  return 0;
}
