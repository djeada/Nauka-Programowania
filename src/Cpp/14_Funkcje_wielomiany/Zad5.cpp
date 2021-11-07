#include <cassert>
#include <vector>

/*
Otrzymujesz liste n wspolczynnikow wielomianu postaci anxn+an-1xn-1+...+a0
oraz liczbe k. Oblicz wspolczynniki wielomianu bedacego k-ta pochodna
otrzymanego wielomianu.
*/

std::vector<int> pochodna(std::vector<int> &wielomian, int k) {
  /**
   * Funkcja oblicza k-ta pochodna wielomianu.
   */
  std::vector<int> wynik;
  std::vector<int> kopia(wielomian);

  for (int i = 0; i < k; i++) {
    wynik.clear();
    int n = kopia.size();
    for (int j = 0; j < n - 1; j++)
      wynik.push_back(kopia[j] * (n - j - 1));
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
