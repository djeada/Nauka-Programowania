/*
Tytul: Operacje arytmetyczne.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci:
a) Ich sume.
b) Roznice drugiej i pierwszej.
c) Ich iloczyn.
d) Iloraz pierwszej przez druga.
e) Reszte z dzielenia pierwszej przez druga.
Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.
Dane wyjsciowe: Liczba calkowita dla wszystkich podpunktow.
Przyklad:
Dla pobranych liczb: 3 i 5, funkcja powinna zwrocic:
a) Sume: 8
b) Roznice: 2
c) Iloczyn: 15
d) Iloraz: 0
e) Reszte z dzielenia: 3

*/
#include <cassert>
#include <string>

int suma(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba + drugaLiczba;
}

int roznica(int pierwszaLiczba, int drugaLiczba) {
  return drugaLiczba - pierwszaLiczba;
}

int iloczyn(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba * drugaLiczba;
}

int reszta(int pierwszaLiczba, int drugaLiczba) {
  return pierwszaLiczba % drugaLiczba;
}

void testSuma() {
  assert(suma(1, 2) == 3);
  assert(suma(2, 2) == 4);
}

void testRoznica() {
  assert(roznica(1, 2) == -1);
  assert(roznica(2, 2) == 0);
}

void testIloczyn() {
  assert(iloczyn(1, 2) == 2);
  assert(iloczyn(2, 2) == 4);
}

void testReszta() {
  assert(reszta(1, 2) == 1);
  assert(reszta(2, 2) == 0);
}

int main() {

  testSuma();
  testRoznica();
  testIloczyn();
  testReszta();

  return 0;
}

