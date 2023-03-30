/*
Tytul: Maks i min
Napisz funkcje, ktora:
a) Dla otrzymanych dwoch liczb zwroci mniejsza.
b) Dla otrzymanych dwoch liczb zwroci wieksza.
c) Dla otrzymanych trzech liczb zwroci najmniejsza.
d) Dla otrzymanych trzech liczb zwroci najwieksza.
Dane wejsciowe:
a) Dwie liczby naturalne.
b) Dwie liczby naturalne.
c) Trzy liczby naturalne.
d) Trzy liczby naturalne.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 1.
b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 3.
c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 1.
d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 3."

*/
#include <cassert>
#include <cmath>

int min2(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba < drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

int maks2(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
}

int min3(int pierwszaLiczba, int drugaLiczba, int trzeciaLiczba) {
  int minAB = pierwszaLiczba < drugaLiczba ? pierwszaLiczba : drugaLiczba;
  return minAB < trzeciaLiczba ? minAB : trzeciaLiczba;
}

int maks3(int pierwszaLiczba, int drugaLiczba, int trzeciaLiczba) {
  int maksAB = pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba;
  return maksAB > trzeciaLiczba ? maksAB : trzeciaLiczba;
}

void testMaks2() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int wynik = pierwszaLiczba;

  assert(maks2(pierwszaLiczba, drugaLiczba) == wynik);
  assert(maks2(drugaLiczba, pierwszaLiczba) == wynik);
}

void testMin2() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int wynik = drugaLiczba;

  assert(min2(pierwszaLiczba, drugaLiczba) == wynik);
  assert(min2(drugaLiczba, pierwszaLiczba) == wynik);
}

void testMaks3() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int trzeciaLiczba = 11;
  int wynik = trzeciaLiczba;

  assert(maks3(pierwszaLiczba, drugaLiczba, trzeciaLiczba) == wynik);
  assert(maks3(drugaLiczba, pierwszaLiczba, trzeciaLiczba) == wynik);
}

void testMin3() {
  int pierwszaLiczba = 7;
  int drugaLiczba = 5;
  int trzeciaLiczba = 11;
  int wynik = drugaLiczba;

  assert(min3(pierwszaLiczba, drugaLiczba, trzeciaLiczba) == wynik);
  assert(min3(drugaLiczba, pierwszaLiczba, trzeciaLiczba) == wynik);
}

int main() {

  testMaks2();
  testMin2();
  testMaks3();
  testMin3();

  return 0;
}

