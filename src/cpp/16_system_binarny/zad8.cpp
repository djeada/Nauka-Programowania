/*
Tytul: Czy liczba jest palindromem?
Tresc: Otrzymujesz dziesietna reprezentacje liczby naturalnej. Sprawdz, czy
reprezentacja binarna otrzymanej liczby jest palindromem. Dane wejsciowe: Liczba
naturalna. Dane wyjsciowe: Wartosc logiczna. Przyklad: Dla otrzymanej liczby 26,
powinna zostac zwrocona wartosc logiczna: Prawda.

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

