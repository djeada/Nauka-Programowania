#include <cassert>
#include <cmath>

/*
Napisz funkcję, która:

a) Dla otrzymanych dwóch liczb, zwraca mniejszą.
b) Dla otrzymanych dwóch liczb, zwróci większą.
c) Dla otrzymanych trzech liczb, zwraca najmniejszą.
d) Dla otrzymanych trzech liczb, zwraca największą.
*/

int min2(int pierwszaLiczba, int drugaLiczba) { return pierwszaLiczba < drugaLiczba ? pierwszaLiczba : drugaLiczba; }

int maks2(int pierwszaLiczba, int drugaLiczba) { return pierwszaLiczba > drugaLiczba ? pierwszaLiczba : drugaLiczba; }

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
