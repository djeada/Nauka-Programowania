/*
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b`
i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

*/
#include <cassert>
#include <cmath>
#include <vector>

std::vector<int> iloczyn(std::vector<int> &wielomianA,
                         std::vector<int> &wielomianB) {
  /**
   * Funkcja zwraca wspolczynniki wielomianu bedacego iloczynem wielomianow a i
   * b.
   */
  std::vector<int> wynik(wielomianA.size() + wielomianB.size() - 1, 0);

  for (unsigned int i = 0; i < wielomianA.size(); i++) {
    for (unsigned int j = 0; j < wielomianB.size(); j++)
      wynik[i + j] += wielomianA[i] * wielomianB[j];
  }

  return wynik;
}

void test1() {
  std::vector<int> wielomianA{5, 0, 10, 6};
  std::vector<int> wielomianB{1, 2, 4};
  std::vector<int> wynik{5, 10, 30, 26, 52, 24};
  assert(iloczyn(wielomianA, wielomianB) == wynik);
}

int main() {
  test1();
  return 0;
}
