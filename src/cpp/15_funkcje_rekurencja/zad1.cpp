/*
Tytul: Liczby naturalne mniejsze od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji stworz napis skladajacy sie
z liczb naturalnych mniejszych od N oddzielonych przecinkami. Dane wejsciowe:
Liczba naturalna N. Dane wyjsciowe: Napis. Przyklad: Dla N = 10, powinien zostac
zwrocony napis: "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0".

*/
#include <cassert>
#include <iostream>

std::string mniejszeLiczby(int n) {
  /**
   *
   */
  if (n <= 0)
    return "";

  if (n == 1)
    return std::to_string(n);

  return std::to_string(n) + ", " + mniejszeLiczbyV1(n - 1);
}

void testMniejszeLiczby() {

  assert(mniejszeLiczby(0) == "");
  assert(mniejszeLiczby(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1");
}

int main() {

  testMniejszeLiczby();

  return 0;
}

