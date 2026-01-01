/*
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b`
(mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników `a + b` w tej samej konwencji

### Przykład

Dla `a = [3, 5, 2]` i `b = [2, -8, 1]` funkcja zwraca:
`[5, -3, 3]`

### Uwagi

* Jeśli listy mają różne długości, wyrównaj je od końca (od wyrazu wolnego).

*/
#include <cassert>
#include <cmath>
#include <vector>

std::vector<int> sumaWielomianow(std::vector<int> &wielomianA,
                                 std::vector<int> &wielomianB) {
  /**
   * Funkcja sumuje dwie listy wielomianow.
   */

  std::vector<int> wynik;

  int min = wielomianA.size() < wielomianB.size() ? wielomianA.size()
                                                  : wielomianB.size();

  for (int i = 0; i < min; i++) {
    wynik.push_back(wielomianA[i] + wielomianB[i]);
  }

  for (int i = min; i < wielomianA.size(); i++) {
    wynik.push_back(wielomianA[i]);
  }

  for (int i = min; i < wielomianB.size(); i++) {
    wynik.push_back(wielomianB[i]);
  }

  return wynik;
}

void test1() {
  std::vector<int> wielomianA{3, 2, 1};
  std::vector<int> wielomianB{8, 9, 2};
  std::vector<int> wynik{11, 11, 3};
  assert(sumaWielomianow(wielomianA, wielomianB) == wynik);
}

int main() {
  test1();

  return 0;
}
