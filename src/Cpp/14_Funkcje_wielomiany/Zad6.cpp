#include <cassert>
#include <cmath>
#include <utility>
#include <vector>

/*
Otrzymujesz liste wspolczynnikow rownania kwadratowego ax^2 + bx + c.
Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
*/

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
