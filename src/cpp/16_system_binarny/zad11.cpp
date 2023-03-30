/*
Tytul: Operacje arytmetyczne.
Tresc: Otrzymujesz dwie liczby naturalne. Uzywajac jedynie operatorow bitowych,
zaimplementuj: a) Dodawanie. b) Odejmowanie. c) Mnozenie. d) Dzielenie. Dane
wejsciowe: Dwie liczby naturalne w kazdym podpunkcie. Dane wyjsciowe: Liczba
naturalna w kazdym podpunkcie. Przyklad: a) Dla otrzymanych liczb: 2 i 3,
powinna zostac zwrocona liczba: 5. b) Dla otrzymanych liczb: 7 i 5, powinna
zostac zwrocona liczba: 2. c) Dla otrzymanych liczb: 4 i 4, powinna zostac
zwrocona liczba: 16. d) Dla otrzymanych liczb: 9 i 3, powinna zostac zwrocona
liczba: 3.

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

