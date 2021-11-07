#include <cassert>

/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz
sume liczb naturalnych mniejszych od N.
*/

int sumaV1(int N) {
  /**
   * Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu
   * przez liczbe x.
   */
  if (N <= 0)
    return 0;

  return N + sumaV1(N - 1);
}

void test1() {
  int N = 10;
  int wynik = 55;

  assert(sumaV1(N) == wynik);
}

int main() {

  test1();

  return 0;
}
