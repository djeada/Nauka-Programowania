/*
Tytul: Liczba Fibonacciego.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz wartosc N-tego wyrazu ciagu Fibonacciego.
Podpowiedz: Ciag Fibonacciego zdefiniowany jest nastepujaco:
* $a_0= 0$,
* $a_1= 1$,
* $a_n= a_{n-1}+a_n-2$.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 7, powinna zostac zwrocona liczba: 13.

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

