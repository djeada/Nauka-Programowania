/*
Tytul: Odwrocenie sasiadujacych bitow.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Zmien miejscami sasiadujace bity w zapisie binarnym tej liczby i zwroc dziesietna reprezentacje wyniku.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby: 9131, powinna zostac zwrocona liczba: 4951.

*/
#include <cassert>

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

