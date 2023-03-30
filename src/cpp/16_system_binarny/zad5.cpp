/*
Tytul: Najblizsza potega dwojki.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Znajdz potege
dwojki wieksza badz rowna tej liczbie. Inaczej: zaokraglij liczbe do najblizszej
potegi dwojki. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Liczba
naturalna. Przyklad: Dla otrzymanej liczby: 111, powinna zostac zwrocona liczba:
128.

*/
#include <cassert>

int znak(int n) {
  /*
   * Funkcja zwraca znak liczby n.
   */
  return (n >> 31) & 0x01;
}

int maks(int a, int b) {
  /*
   * Funkcja zwraca maksimum dwoch liczb.
   * dla a >= b: znak_a = 1, znak_b = 0;
   * dla a < b: znak_a = 0, znak_b = 1;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakA * a + znakB * b;
}

int min(int a, int b) {
  /*
   * Funkcja zwraca minimum dwoch liczb.
   * dla a >= b: znak_a = 0, znak_b = 1;
   * dla a < b: znak_a = 1, znak_b = 0;
   */
  int znakB = znak(a - b);
  int znakA = znakB ^ 1;
  return znakB * a + znakA * b;
}

void testMaks() {
  int a = 10;
  int b = 8;
  int wynik = a;

  assert(maks(a, b) == wynik);
}

void testMin() {
  int a = 10;
  int b = 8;
  int wynik = b;

  assert(min(a, b) == wynik);
}

int main() {

  testMaks();
  testMin();

  return 0;
}

