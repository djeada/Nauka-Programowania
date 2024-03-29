/*
Tytul: NWD.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najwiekszy wspolny dzielnik.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 60 i 45, funkcja powinna zwrocic liczbe 15.

*/
#include <cassert>

int nwdV1(int a, int b) {

  if (b == 0)
    return a;

  return nwdV1(b, a % b);
}

int nwdV2(int a, int b) {

  int c;

  while (b != a % b) {
    c = b;
    b = a % b;
    a = c;

    if (b == 0)
      break;
  }

  return a;
}

void testNwd1() {
  assert(nwdV1(12, 15) == 3);
  assert(nwdV1(15, 12) == 3);
  assert(nwdV1(15, 0) == 15);
  assert(nwdV1(0, 15) == 15);
}

void testNwd2() {
  assert(nwdV2(12, 15) == 3);
  assert(nwdV2(15, 12) == 3);
  assert(nwdV2(15, 0) == 15);
  assert(nwdV2(0, 15) == 15);
}

int main() {

  testNwd1();
  testNwd2();

  return 0;
}

