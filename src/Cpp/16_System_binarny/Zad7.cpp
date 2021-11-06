#include <cassert>

/*
Otrzymujesz dziesiętną reprezentację liczby naturalnej. 
Zamień miejscami sąsiadujące bity w zapisie binarnym 
otrzymanej liczbie. Zwróć dziesiętną reprezentację wyniku.
*/

int zamienSasiadow(int liczba) {
  /*
  * Funkcja zamienia sasiadujace bity w binarnym zapisie liczby.
  */
  int parzyste = liczba & 0xAAAAAAAA;
  int nieparzyste = liczba & 0x55555555;

  parzyste >>= 1;
  nieparzyste <<= 1;

  return parzyste | nieparzyste;
}

void test1() {
  int liczba = 9131;
  int wynik = 4951;

  assert(zamienSasiadow(liczba) == wynik);
}

int main() {

  test1();

  return 0;
}
