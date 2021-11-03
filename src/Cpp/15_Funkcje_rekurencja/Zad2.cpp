#include <cassert>

/*
Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz 
sumę liczb naturalnych mniejszych od N.
*/

int sumaV1(int N) {
  /**
   * Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu przez liczbę x.
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
