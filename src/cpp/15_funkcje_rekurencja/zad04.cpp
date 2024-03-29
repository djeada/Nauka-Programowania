/*
Tytul: Silnia.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz silnie z tej liczby.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 3, powinna zostac zwrocona liczba: 6.

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

