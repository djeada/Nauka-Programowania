#include <cassert>

/*
Napisz funkcje, ktora dla otrzymanych dwoch liczb pierwszaLiczba oraz
drugaLiczba zamieni wartosci miejscami. Po wykonaniu funkcji zmienna
pierwszaLiczba, powinna przechowywac dawna wartosc zmiennej drugaLiczba,
pierwszaLiczba zmienna drugaLiczba powinna przechowywac dawna wartosc zmiennej
pierwszaLiczba.
*/

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
