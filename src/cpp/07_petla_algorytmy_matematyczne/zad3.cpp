/*
Tytul: Mnozenie i dzielenie.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych a i b, przy
pomocy dodawania lub odejmowania oraz petli, obliczy: a) iloczyn tych liczb b)
iloraz liczby a przez liczbe b Dane wejsciowe: dwie liczby naturalne Dane
wyjsciowe: liczba naturalna Przyklad: Dla pobranych liczb 3 i 2, funkcja powinna
zwrocic liczbe: a) 6; b) 2.

*/
#include <cassert>

int iloczyn(int mnozna, int mnoznik) {

  int znak = 1;

  if (mnozna < 0) {
    znak = -1;
    mnozna = -mnozna;
  }
  if (mnoznik < 0) {
    znak = -1;
    mnoznik = -mnoznik;
  }
  int wynik = 0;
  for (int i = 0; i < mnoznik; i++)
    wynik += mnozna;

  return wynik * znak;
}

int iloraz(int dzielna, int dzielnik) {
  int znak = 1;

  if (dzielna < 0) {
    znak = -1;
    dzielna = -dzielna;
  }

  if (dzielnik < 0) {
    znak *= -1;
    dzielnik = -dzielnik;
  }

  int wynik = 0;
  while (dzielna >= dzielnik) {
    dzielna -= dzielnik;
    wynik++;
  }

  return wynik * znak;
}

void testIloczyn() {
  assert(iloczyn(2, 3) == 6);
  assert(iloczyn(3, 2) == 6);
  assert(iloczyn(-2, 3) == -6);
  assert(iloczyn(3, -2) == -6);
  assert(iloczyn(-2, -3) == 6);
}

void testIloraz() {
  assert(iloraz(6, 3) == 2);
  assert(iloraz(3, 6) == 0.5);
  assert(iloraz(6, -3) == -2);
  assert(iloraz(-3, 6) == -0);
  assert(iloraz(-6, -3) == 2);
}

int main() {

  testIloczyn();
  testIloraz();

  return 0;
}

