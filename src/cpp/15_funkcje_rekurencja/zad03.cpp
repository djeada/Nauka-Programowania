/*
Tytul: Potega.
Tresc: Otrzymujesz dwie liczby, a i b. Przy uzyciu rekurencji oblicz a podniesione do b.
Dane wejsciowe: Dwie liczby naturalne a i b.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla a = 2 i b = 3, powinna zostac zwrocona liczba: 8.

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

