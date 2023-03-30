/*
Tytul: Silnia.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz silnie z tej liczby.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 3, powinna zostac zwrocona liczba: 6.

*/
#include <cassert>

int potegaV1(int a, int b) {
  /**
   *
   */
  if (b == 0)
    return 1;

  return a * potegaV1(a, b - 1);
}

void test1() {
  int a = 3;
  int b = 2;
  int wynik = 9;

  assert(potegaV1(a, b) == wynik);
}

int main() {

  test1();

  return 0;
}

