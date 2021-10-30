#include <cassert>

/*
Napisz funkcję, która przy pomocy pętli obliczy silnię 
otrzymanej liczby.
*/

int silnia(int liczba) {

  int wynik = 1;

  while (liczba > 0) {
    wynik *= liczba;
    liczba--;
  }

  return wynik;
}

void testSilnia() {
  assert(silnia(0) == 1);
  assert(silnia(1) == 1);
  assert(silnia(2) == 2);
  assert(silnia(3) == 6);
  assert(silnia(4) == 24);
  assert(silnia(5) == 120);
}

int main() {

  testSilnia();

  return 0;
}
