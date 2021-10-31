#include <cassert>
#include <string>

/*
Napisz funkcje, ktora zwroci:

a) Liczbe 3.
b) Napis “Tak”.
c) Wartosc logiczna Prawda.
*/

int zwroc3() { return 3; }

std::string zwrocTak() { return "Tak"; }

bool zwrocTrue() { return true; }

void testZwroc3() { assert(zwroc3() == 3); }

void testZwrocTak() { assert(zwrocTak() == "Tak"); }

void testZwrocTrue() { assert(zwrocTrue()); }

int main() {

  testZwroc3();
  testZwrocTak();
  testZwrocTrue();

  return 0;
}
