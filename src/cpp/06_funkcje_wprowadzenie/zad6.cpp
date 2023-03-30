/*
Tytul: Cyfry liczby
Tresc: Napisz funkcje, ktora dla otrzymanej liczby obliczy sume jej cyfr.
Dane wejsciowe: liczba naturalna
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranej liczby 13231, funkcja powinna zwrocic liczbe 10.

*/
#include <cassert>
#include <cmath>

int sumaCyfr(int liczba) {
  int suma = 0;

  while (liczba > 0) {
    suma += (liczba % 10);
    liczba /= 10;
  }

  return suma;
}

void testSumaCyfr() {
  assert(sumaCyfr(123) == 6);
  assert(sumaCyfr(0) == 0);
  assert(sumaCyfr(1) == 1);
}

int main() {

  testSumaCyfr();

  return 0;
}

