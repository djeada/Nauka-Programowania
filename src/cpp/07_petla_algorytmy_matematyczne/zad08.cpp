/*
Tytul: Naiwny test pierwszosci
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej sprawdzi, czy jest ona liczba pierwsza.
Dane wejsciowe: liczba naturalna
Dane wyjsciowe: wartosc logiczna
Przyklad:
Dla otrzymanej liczby 7, funkcja powinna zwrocic wartosc logiczna prawda. Dla otrzymanej liczby 2, funkcja powinna zwrocic wartosc logiczna prawda.

*/
#include <cassert>
#include <cmath>

bool pierwsza(int n) {

  if (n <= 1)
    return false;

  if (n % 2 == 0 && n != 2)
    return false;

  for (int i = 3; i <= sqrt((double)n); i += 2) {
    if (n % i == 0)
      return false;
  }

  return true;
}

void testPierwsza() {
  assert(pierwsza(2));
  assert(pierwsza(3));
  assert(pierwsza(5));
  assert(pierwsza(7));
  assert(pierwsza(11));
  assert(!pierwsza(14));
  assert(!pierwsza(15));
  assert(!pierwsza(16));
}

int main() {

  testPierwsza();

  return 0;
}

