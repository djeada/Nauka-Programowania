/*
Tytul: Zwroc stala.
Tresc: Napisz funkcje, ktora zwroci:
a) Liczbe 3.
b) Napis "Tak".
c) Wartosc logiczna Prawda.
Dane wejsciowe: Brak.
Dane wyjsciowe:
a) Liczba 3.
b) Napis "Tak".
c) Wartosc logiczna Prawda.

*/
#include <cassert>
#include <string>

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

