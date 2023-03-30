/*
Tytul: Obliczenie wartosci wielomianu w punkcie.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n +
a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna x. Znajdz wartosc wielomianu w
podanym punkcie. Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla listy wspolczynnikow [3, 2, 1] i liczby x = 1, zostanie zwrocona liczba 6.

*/
#include <cassert>
#include <cmath>
#include <vector>

int wartoscWielomianu(std::vector<int> &wielomian, int x) {
  /**
   * Funkcja zwraca wartosc wielomianu w punkcie x.
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

