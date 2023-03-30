/*
Tytul: NWW.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najmniejsza wspolna wielokrotnosc.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 7 i 9, funkcja powinna zwrocic liczbe 63.

*/
#include <cassert>

int nwd(int a, int b) {

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

int nww(int a, int b) { return a * b / nwd(a, b); }

void testNww() {
  assert(nww(12, 15) == 60);
  assert(nww(12, 16) == 48);
  assert(nww(12, 18) == 36);
}

int main() {

  testNww();

  return 0;
}

