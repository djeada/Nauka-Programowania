/*
Tytul: Zamien wartosci miejscami.
Tresc: Napisz funkcje, ktora zamieni wartosci zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywac wartosc zmiennej b, a zmienna b powinna przechowywac wartosc zmiennej a.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla otrzymanych liczb: 8 i 5, powinny zostac zwrocone liczby 5 i 8.

*/
#include <cassert>

void swap(int &pierwszaLiczba, int &drugaLiczba) {
  int c = pierwszaLiczba;
  pierwszaLiczba = drugaLiczba;
  drugaLiczba = c;
}

void testSwap() {
  int pierwszaLiczba = 1;
  int drugaLiczba = 2;
  swap(pierwszaLiczba, drugaLiczba);
  assert(pierwszaLiczba == 2);
  assert(drugaLiczba == 1);
}

int main() {

  testSwap();

  return 0;
}

