/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę
`x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

*/
#include <cassert>
#include <cmath>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
int wartoscWielomianu(std::vector<int> &wielomian, int x) {
  /**
   * Funkcja zwraca wartosc wielomianu w punkcie x.
   */
  int n = wielomian.size();
  int wynik = 0;

  for (int i = 0; i < n; i++) wynik += wielomian[i] * pow(x, n - i);

  return wynik;
}

void test1() {
  std::vector<int> wielomian{3, 2, 1};
  int x = 1;
  int wynik = 6;
  assert(wartoscWielomianu(wielomian, x) == wynik);
}

int main() {
  test1();

  return 0;
}
