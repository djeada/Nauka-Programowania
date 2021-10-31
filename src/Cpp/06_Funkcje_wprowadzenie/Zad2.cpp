#include <cassert>
#include <string>

/*
Pobierz dwie liczby od użytkownika. Napisz funkcję, która dla otrzymanych dwóch
liczb zwróci:

a) Ich sumę.
b) Różnicę drugiej i pierwszej.
c) Ich iloczyn.
d) Iloraz pierwszej przez drugą.
e) Resztę z dzielenia pierwszej przez drugą.
*/

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
