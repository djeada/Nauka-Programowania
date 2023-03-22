#include <cassert>
#include <cmath>
#include <vector>

/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci a_nx^n + a_(n-1)x^(n-1) +
... + a_0 oraz liczbe x. Oblicz wspolczynniki wielomianu bedacego wynikiem
przemnozenia otrzymanego wielomianu przez liczbe x.
*/

std::vector<int> iloczyn(std::vector<int> &wielomian, int x) {
  /**
   * Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu
   * przez liczbe x.
   */
  std::vector<int> wynik;

  for (auto &liczba : wielomian)
    wynik.push_back(liczba * x);

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