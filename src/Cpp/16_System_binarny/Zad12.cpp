#include <algorithm>
#include <cassert>

/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.
Oblicz dlugosc najdluzszego ciagu zer w jej binarnej reprezentacji.
*/

int najdluzszyCiagZer(int liczba) {
  /*
   * Funkcja zwraca dlugosc najdluzszego ciagu zer w dziesietnej
   * reprezentacji liczby binarnej.
   */
  if (liczba == 0)
    return 1;

  int wynik = 0;
  int pom = 0;

  while (liczba != 0) {
    int reszta = liczba % 2;
    liczba /= 2;
    if (reszta == 1) {
      wynik = std::max(wynik, pom);
      pom = 0;
    } else
      pom++;
  }
  return std::max(wynik, pom);
}

void testNajdluzszyCiagZer() {
  assert(najdluzszyCiagZer(111) == 1);
  assert(najdluzszyCiagZer(8219) == 8);
}

int main() {

  test1();
  test2();

  return 0;
}
