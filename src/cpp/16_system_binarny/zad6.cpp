/*
Tytul: Zmiana wielkosci liter.
Tresc: Otrzymujesz napis. Zaimplementuj nastepujace operacje przy uzyciu
operatorow bitowych: a) Zamien wielkie litery na male litery. b) Zamien male
litery na wielkie litery. c) Zamien male litery na wielkie litery i wielkie
litery na male litery. Dane wejsciowe: Napis. Dane wyjsciowe: Napis. Przyklad:
a) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "test".
b) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "TEST".
c) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "tEST".

*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <string>

int naDziesietny(std::string liczba, int staraPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie dziesietnym.
   */

  int reprezentacjaDziesietna = 0;

  for (int i = liczba.size() - 1; i >= 0; i--) {

    if (liczba[i] >= 'A' && liczba[i] < 'Z')
      reprezentacjaDziesietna +=
          (liczba[i] - 'A' + 10) * pow(staraPodstawa, (liczba.size() - 1 - i));

    else
      reprezentacjaDziesietna +=
          (liczba[i] - '0') * pow(staraPodstawa, (liczba.size() - 1 - i));
  }

  return reprezentacjaDziesietna;
}

void zmianaPodstawy(std::string &liczba, int staraPodstawa, int nowaPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie dziesietnym.
   */
  if (staraPodstawa > (10 + 'Z' - 'A'))
    throw std::invalid_argument("Podstawa systemu nie moze byc wieksza niz 36");

  int reprezentacjaDziesietna = naDziesietny(liczba, staraPodstawa);
  liczba = "";
  podstawa = nowaPodstawa;

  while (reprezentacjaDziesietna > 0) {
    int reszta = reprezentacjaDziesietna % podstawa;
    reprezentacjaDziesietna /= podstawa;

    char nowyZnak = '0' + reszta;

    if (nowyZnak > '9')
      nowyZnak = 'A' + (nowyZnak - '9') - 1;

    liczba += nowyZnak;
  }

  reverse(liczba.begin(), liczba.end());
}

void testZmianaPodstawy() {
  std::string liczba = "4301";
  std::string wynik = "1003031";
  zmianaPodstawy(liczba, 10, 4);

  assert(liczba == wynik);
}

int main() {

  testZmianaPodstawy();

  return 0;
}

