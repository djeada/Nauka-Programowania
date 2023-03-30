/*
Tytul: Liczba zer i jedynek w reprezentacji binarnej.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej.
a) Oblicz, ile zer zawiera binarna reprezentacja otrzymanej liczby.
b) Oblicz, ile jedynek zawiera binarna reprezentacja otrzymanej liczby.
Dane wejsciowe: Liczba naturalna w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 0.
b) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 2.

*/
#include <algorithm>
#include <cassert>

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

