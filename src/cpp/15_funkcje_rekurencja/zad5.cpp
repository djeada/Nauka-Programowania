/*
Tytul: N-ty wyraz ciagu danego wzorem rekurencyjnym.
Tresc: Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem
rekurencyjnym:
* $a_1 = 1$
* $a_n = 1+2*a_{n-1}$
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 5, powinna zostac zwrocona liczba: 31.

*/
#include <cassert>

int fibonnaciV1(int n) {
  /**
   *
   */
  if (n == 0 || n == 1)
    return n;

  return fibonnaciV1(n - 1) + fibonnaciV1(n - 2);
}

int fibonnaciV2(int n) {
  static int pom[100] = {0};

  if (pom[n] != 0)
    return pom[n];

  if (n == 0 || n == 1) {
    pom[n] = n;
    return pom[n];
  }

  pom[n] = fibonnaciV2(n - 1) + fibonnaciV2(n - 2);

  return pom[n];
}

void test1() {
  int n = 7;
  int wynik = 13;

  assert(fibonnaciV1(n) == wynik);
  assert(fibonnaciV2(n) == wynik);
}

int main() {

  test1();

  return 0;
}

