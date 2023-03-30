/*
Tytul: Obliczenie sumy wielomianow.
Tresc: Otrzymujesz dwie listy n wspolczynnikow wielomianu w postaci $a_nx^n +
a_{n-1}x^{n-1} + ... + a_0$. Oblicz wspolczynniki wielomianu bedacego suma
otrzymanych wielomianow. Dane wejsciowe: Dwie listy liczb naturalnych. Dane
wyjsciowe: Lista liczb naturalnych. Przyklad: Dla otrzymanych dwoch list [3, 5,
2] oraz [2, -8, 1], zostanie zwrocona lista [5, -3, 3].

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

