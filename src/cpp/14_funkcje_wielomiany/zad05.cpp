/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę
naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `k` — liczba naturalna

### Wyjście (zwracana wartość)

* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy:
`[0]`.

*/
#include <cassert>
#include <vector>

// Zlozonosc Czasowa: O(k * n)
// Zlozonosc Pamieciowa: O(n)
std::vector<int> pochodna(std::vector<int> &wielomian, int k) {
  /**
   * Funkcja oblicza k-ta pochodna wielomianu.
   */
  std::vector<int> wynik;
  std::vector<int> kopia(wielomian);

  for (int i = 0; i < k; i++) {
    wynik.clear();
    int n = kopia.size();
    for (int j = 0; j < n - 1; j++) wynik.push_back(kopia[j] * (n - j - 1));
    kopia = wynik;
  }

  return wynik;
}

void test1() {
  std::vector<int> wielomian{4, -3, 2};
  int k = 1;
  std::vector<int> wynik{8, -3};
  assert(pochodna(wielomian, k) == wynik);
}

void test2() {
  std::vector<int> wielomian{13, -6, 0, -1, -1};
  int k = 2;
  std::vector<int> wynik{156, -36, 0};
  assert(pochodna(wielomian, k) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
