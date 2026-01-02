/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę
`k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego
współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

*/
#include <cassert>
#include <cmath>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(n)
std::vector<int> iloczyn(std::vector<int> &wielomian, int x) {
  /**
   * Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu
   * przez liczbe x.
   */
  std::vector<int> wynik;

  for (auto &liczba : wielomian) wynik.push_back(liczba * x);

  return wynik;
}

void test1() {
  std::vector<int> wielomian{3, 2, 1};
  int x = 2;
  std::vector<int> wynik{6, 4, 2};
  assert(iloczyn(wielomian, x) == wynik);
}

int main() {
  test1();

  return 0;
}
