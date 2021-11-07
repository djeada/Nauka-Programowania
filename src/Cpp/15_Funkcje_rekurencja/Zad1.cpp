#include <cassert>
#include <iostream>

/*
Otrzymujesz liczbe N. Przy uzyciu rekurencji zbuduj napis skladajacy
sie z liczb naturalnych mniejszych od N oddzielonych przecinkami.
*/

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
