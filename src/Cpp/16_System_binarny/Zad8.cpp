#include <cassert>

/*
Otrzymujesz dziesiętną reprezentację liczby naturalnej. Znajdź potęgę 
dwójki większą bądź równą otrzymanej liczbie. Inaczej: zaokrąglij liczbę 
do następnej potęgi dwójki.
*/

int nastepnaPotegaDwojkiV1(int liczba) {
  /*
  * Funkcja zwraca następną potęgę dwójki większą bądź równą liczbie.
  * Zasada działania opiera się na zmniejszaniu liczby, aż liczba będzie podzielna przez 2.
  */
  if (liczba <= 0)
    return 0;

  if (liczba == 1)
    return 2;

  liczba--;

  while (liczba & (liczba - 1))
    liczba &= liczba - 1;

  return liczba << 1;
}

int nastepnaPotegaDwojkiV2(int liczba) {
  /*
  * Funkcja zwraca następną potęgę dwójki większą bądź równą liczbie.
  * Zasada działania opiera się na obliczeniu następnych potęg dwójki, 
  * aż otrzymamy liczbę większą lub równą podanej liczbie.
  */
  if (liczba <= 0)
    return 0;

  int potega = 2;

  while (liczba > 2) {
    liczba >>= 1;
    potega <<= 1;
  }

  return potega;
}

void testNastepnaPotegaDwojkiV1() {
  assert(nastepnaPotegaDwojkiV1(111) == 128);
  assert(nastepnaPotegaDwojkiV1(-30) == 0);
  assert(nastepnaPotegaDwojkiV1(1) == 2);
}

void testNastepnaPotegaDwojkiV2() {
  assert(nastepnaPotegaDwojkiV2(111) == 128);
  assert(nastepnaPotegaDwojkiV2(-30) == 0);
  assert(nastepnaPotegaDwojkiV2(1) == 2);
}

int main() {

  testNastepnaPotegaDwojkiV1();
  testNastepnaPotegaDwojkiV2();

  return 0;
}
