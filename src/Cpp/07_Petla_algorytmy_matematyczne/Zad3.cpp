#include <cassert>

/*
Napisz funkcje, ktora dla otrzymanych dwoch liczb, przy pomocy
dodawania badz odejmowania oraz petli obliczy:

a) Iloczyn otrzymanych liczb.
b) Iloraz pierwszej liczby przez druga liczbe.
*/

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
