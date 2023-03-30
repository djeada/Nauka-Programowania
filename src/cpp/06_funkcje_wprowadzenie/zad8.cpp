/*
Tytul: Zaokraglanie w dol.
Tresc: Napisz funkcje, ktora zaokragli iloraz dwoch liczb naturalnych do
najblizszej liczby calkowitej w dol, bez uzycia operatorow '/' i '%'. Dane
wejsciowe: dwie liczby naturalne Dane wyjsciowe: liczba naturalna Przyklad: Dla
otrzymanych liczb 7 i 2, funkcja powinna zwrocic liczbe 3.

*/
#include <cassert>
#include <limits>

int podziel(int dzielna, int dzielnik) {

  int znak = 1;
  int licznik = 0;

  if (dzielnik == 0)
    return std::numeric_limits<int>::signaling_NaN();

  if (dzielna == 0)
    return 0;

  if (dzielna < 0) {
    znak = -1;
    dzielna = -dzielna;
  }

  if (dzielnik < 0) {
    znak *= -1;
    dzielnik = -dzielnik;
  }

  if (znak == 1) {
    licznik = 0;
    while (dzielna >= dzielnik) {
      dzielna -= dzielnik;
      licznik += 1;
    }
  }

  else {
    licznik = 1;
    while (dzielna > dzielnik) {
      dzielna -= dzielnik;
      licznik += 1;
    }
  }

  return licznik * znak;
}

void testPodziel() {
  assert(podziel(0, 1) == 0);
  assert(podziel(1, 1) == 1);
  assert(podziel(25, 5) == 5);
  assert(podziel(25, -5) == -5);
  assert(podziel(-25, 5) == -5);
  assert(podziel(-25, -5) == 5);
  assert(podziel(25, 0) == std::numeric_limits<int>::signaling_NaN());
  assert(podziel(0, 0) == std::numeric_limits<int>::signaling_NaN());
}

int main() {

  testPodziel();

  return 0;
}

