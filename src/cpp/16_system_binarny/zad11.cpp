/*
Tytul: Czy liczba jest palindromem?
Tresc: Otrzymujesz dziesietna reprezentacje liczby naturalnej. Sprawdz, czy reprezentacja binarna otrzymanej liczby jest palindromem.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanej liczby 26, powinna zostac zwrocona wartosc logiczna: Prawda.

*/
#include <bitset>
#include <cassert>

const int liczbaBitow = 8;

bool czyPalindrom(int liczba) {
  /*
   * Funkcja sprawdza czy podana liczba jest palindromem.
   */
  std::bitset<liczbaBitow> bity = liczba;

  for (int i = 0; i < liczbaBitow / 2 - 1; i++) {
    if (bity[i] ^ bity[liczbaBitow - 1 - i])
      return false;
  }

  return true;
}

void testCzyPalindrom() {
  assert(czyPalindrom(231));
  assert(!czyPalindrom(17));
}

int main() {

  testCzyPalindrom();
  return 0;
}

