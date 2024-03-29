/*
Tytul: Znajdz najdluzsze/najkrotsze slowo w zdaniu.
Tresc: Otrzymasz napis reprezentujacy zdanie. Znajdz:
a) najdluzsze slowo w zdaniu,
b) najkrotsze slowo w zdaniu.
Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe:
a) Napis.
b) Napis.
Przyklad:
a) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "Kaczka".
b) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "lubi".

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

std::string najdluzsze(std::string &napis) {
  std::string wynik;
  unsigned int dlugosc = 0;
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);

      if (slowo.size() > dlugosc) {
        wynik = slowo;
        dlugosc = slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (slowo.size() > dlugosc) {
      wynik = slowo;
      dlugosc = slowo.size();
    }
  }

  return wynik;
}

std::string najkrotsze(std::string &napis) {
  std::string wynik;
  unsigned int dlugosc = napis.size();
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);

      if (slowo.size() < dlugosc) {
        wynik = slowo;
        dlugosc = slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (slowo.size() < dlugosc) {
      wynik = slowo;
      dlugosc = slowo.size();
    }
  }

  return wynik;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  std::string wynik = "Kaczka";
  assert(najdluzsze(napis) == wynik);
}

void test2() {
  std::string napis = "Kaczka lubi wiosne.";
  std::string wynik = "lubi";
  assert(najkrotsze(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

