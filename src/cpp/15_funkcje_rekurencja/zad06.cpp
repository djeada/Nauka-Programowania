/*
Tytul: N-ty wyraz ciagu danego wzorem rekurencyjnym.
Tresc: Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem rekurencyjnym:
* $a_1 = 1$
* $a_n = 1+2*a_{n-1}$
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 5, powinna zostac zwrocona liczba: 31.

*/
#include <cassert>

int ciagV1(int n) {
  /**
   *
   */
  if (n == 1)
    return 1;

  return 1 + ciagV1(n - 1) * 2;
}

void test1() {
  int n = 5;
  int wynik = 31;

  assert(ciagV1(n) == wynik);
}

int main() {

  test1();

  return 0;
}

