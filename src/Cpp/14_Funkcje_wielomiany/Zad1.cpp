#include <cassert>
#include <cmath>
#include <vector>

/*
Otrzymujesz listę n współczynników wielomianu postaci: a_nx^n + a_(n-1)x^(n-1) + ... + a_0
oraz liczbę naturalną x. Znajdź wartość wielomianu w zadanym punkcie.
*/


int wartoscWielomianu(std::vector<int> &wielomian, int x) {
  /**
   * Funkcja zwraca wartość wielomianu w punkcie x.
   */
  int n = wielomian.size();
  int wynik = 0;

  for (int i = 0; i < n; i++)
    wynik += wielomian[i] * pow(x, n - i);

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
