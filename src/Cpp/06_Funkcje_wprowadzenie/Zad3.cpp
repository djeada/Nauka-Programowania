#include <cassert>
#include <cmath>

/*
Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora dla otrzymanych
dwoch liczb odpowie na nastepujace pytanie:

a) Czy pierwsza liczba jest wieksza od drugiej liczby?
b) Czy suma liczb jest mniejsza niz 10?
c) Czy obie liczby sa nieparzyste?
d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do
kwadratu?
*/

bool pierwszaWieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba;
}

bool sumaMniejsza10(int pierwszaLiczba, int drugaLiczba) {
  int suma = pierwszaLiczba + drugaLiczba;
  return suma < 10;
}

bool obieNieparzyste(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba % 2 == 1 && drugaLiczba % 2 == 1;
}

int wieksza(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

bool wiekszaMniejszaPierwszaKwadrat(int pierwszaLiczba, int drugaLiczba) {
  return wieksza(pierwszaLiczba, drugaLiczba) < pow(pierwszaLiczba, 2);
}

void testPierwszaWieksza() {
  assert(!pierwszaWieksza(1, 2));
  assert(pierwszaWieksza(2, 1));
}

void testSumaMniejsza10() {
  assert(!sumaMniejsza10(1, 2));
  assert(sumaMniejsza10(1, 9));
  assert(sumaMniejsza10(9, 1));
}

void testObieNieparzyste() {
  assert(!obieNieparzyste(1, 2));
  assert(obieNieparzyste(1, 1));
  assert(obieNieparzyste(2, 2));
}

void testWiekszaMniejszaPierwszaKwadrat() {
  assert(!wiekszaMniejszaPierwszaKwadrat(1, 2));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 1));
  assert(wiekszaMniejszaPierwszaKwadrat(2, 2));
}

int main() {

  testPierwszaWieksza();
  testSumaMniejsza10();
  testObieNieparzyste();
  testWiekszaMniejszaPierwszaKwadrat();

  return 0;
}
