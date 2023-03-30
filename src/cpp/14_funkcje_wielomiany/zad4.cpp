/*
Tytul: Mnozenie wielomianow.
Tresc: Otrzymujesz dwie listy n wspolczynnikow wielomianu w postaci $a_nx^n +
a_{n-1}x^{n-1} + ... + a_0$. Oblicz wspolczynniki wielomianu bedacego iloczynem
otrzymanych wielomianow. Dane wejsciowe: Dwie listy liczb naturalnych. Dane
wyjsciowe: Lista liczb naturalnych. Przyklad: Dla otrzymanych dwoch list: [5, 0,
10, 6] oraz [1, 2, 4], zostanie zwrocona lista: [5, 10, 30, 26, 52, 24].

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

