#include <cassert>

/*
Otrzymujesz dwie liczby naturalne. Oblicz ile bitow
nalezy odwrocic, aby zamienic liczbe A w liczbe B.
*/

int bityDoZmiany(int liczbaA, int liczbaB) {
  /*
   * Funkcja zwraca ilosc bitow do zmiany liczby A w liczbe B.
   */
  int n = liczbaA ^ liczbaB;

  int licznik = 0;
  while (n != 0) {
    n &= (n - 1);
    licznik++;
  }

  return licznik;
}

void testBityDoZmiany() {
  int liczbaA = 34;
  int liczbaB = 73;
  int wynik = 5;

  assert(bityDoZmiany(liczbaA, liczbaB) == wynik);
}

int main() {

  testBityDoZmiany();

  return 0;
}
