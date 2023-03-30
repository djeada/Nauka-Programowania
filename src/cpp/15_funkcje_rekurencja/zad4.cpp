/*
Tytul: Liczba Fibonacciego.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz wartosc N-tego wyrazu
ciagu Fibonacciego. Podpowiedz: Ciag Fibonacciego zdefiniowany jest nastepujaco:
* $a_0= 0$,
* $a_1= 1$,
* $a_n= a_{n-1}+a_n-2$.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 7, powinna zostac zwrocona liczba: 13.

*/
#include <cassert>

int silniaV1(int n) {
  /**
   *
   */
  if (n == 0 || n == 1)
    return 1;

  return n * silniaV1(n - 1);
}

void test1() {
  int n = 3;
  int wynik = 6;

  assert(silniaV1(n) == wynik);
}

int main() {
  test1();

  return 0;
}

