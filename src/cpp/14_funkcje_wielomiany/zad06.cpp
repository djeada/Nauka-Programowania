/*
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a,
b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.

### Wejście (argumenty funkcji)

* `coef` — lista trzech liczb `[a, b, c]`

### Wyjście (zwracana wartość)

* lista liczb zmiennoprzecinkowych:

  * jeśli `Δ < 0` → pusta lista `[]`
  * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
  * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)

### Przykład

Dla `[1, 2, 1]` funkcja zwraca:
`[-1.0, -1.0]`

### Ograniczenia / gwarancje

* Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).

### Uwagi

* Licz `Δ = b^2 - 4ac`.
* Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.

*/
#include <cassert>
#include <cmath>
#include <utility>
#include <vector>

std::pair<double, double> pierwiastki(std::vector<int> &wspolczynniki) {
  /**
   * Funkcja zwraca liste miejsc zerowych rownania kwadratowego.
   */

  if (wspolczynniki.size() != 3) {
    throw std::invalid_argument("Podano nieprawidlowe wspolczynniki.");
  }

  std::pair<double, double> wynik;

  int delta = wspolczynniki[1] * wspolczynniki[1] -
              4 * wspolczynniki[0] * wspolczynniki[2];

  if (delta > 0) {
    wynik.first = (-wspolczynniki[1] + sqrt(delta)) / (2 * wspolczynniki[0]);
    wynik.second = (-wspolczynniki[1] - sqrt(delta)) / (2 * wspolczynniki[0]);
  }

  else if (delta == 0) {
    wynik.first = -wspolczynniki[1] / (2 * wspolczynniki[0]);
    wynik.second = -wspolczynniki[1] / (2 * wspolczynniki[0]);
  }

  return wynik;
}

void test1() {
  std::vector<int> lista{1, 2, 1};
  std::pair<double, double> wynik{-1, -1};
  assert(pierwiastki(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, -4, 5};
  std::pair<double, double> wynik;
  assert(pierwiastki(lista) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
