/*
Tytul: Najblizsza potega dwojki.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Znajdz potege dwojki wieksza badz rowna tej liczbie. Inaczej: zaokraglij liczbe do najblizszej potegi dwojki.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby: 111, powinna zostac zwrocona liczba: 128.

*/
#include <cassert>

int nastepnaPotegaDwojkiV1(int liczba) {
  /*
   * Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
   * Zasada dzialania opiera sie na zmniejszaniu liczby, az liczba bedzie
   * podzielna przez 2.
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
   * Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
   * Zasada dzialania opiera sie na obliczeniu nastepnych poteg dwojki,
   * az otrzymamy liczbe wieksza lub rowna podanej liczbie.
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

