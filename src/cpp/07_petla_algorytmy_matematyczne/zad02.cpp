/*
Tytul: Podnies a do b.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb obliczy ile wynosi a podniesione do b, przy pomocy petli.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranych liczb 3 i 5, funkcja powinna zwrocic liczbe 243.

*/
#include <cassert>
#include <cmath>

double potega(int podstawa, int wykladnik) {
  int wynik = 1;
  for (int i = 0; i < abs(wykladnik); i++)
    wynik *= podstawa;

  if (wykladnik < 0)
    return 1 / wynik;

  return wynik;
}

void testPotega() {
  assert(potega(2, 3) == 8);
  assert(potega(2, -3) == 0.125);
}

int main() {

  testPotega();

  return 0;
}

