/*
Tytul: Srednia dlugosc slow w zdaniu.
Tresc: Otrzymasz napis reprezentujacy zdanie. Oblicz srednia dlugosc slow w zdaniu. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "Zepsuty rower.", powinna zostac zwrocona liczba: 6.

*/
#include <algorithm>
#include <cassert>
#include <string>

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

int srednia(const std::string &napis) {
  unsigned int calk_dlugosc = 0;
  unsigned int n = 0;
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      if (!slowo.empty()) {
        n++;
        calk_dlugosc += slowo.size();
      }
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (!slowo.empty()) {
      n++;
      calk_dlugosc += slowo.size();
    }
  }

  return calk_dlugosc / n;
}

void test1() {
  std::string napis = "Kaczka lubi wiosne.";
  int wynik = 5;
  assert(srednia(napis) == wynik);
}

void test2() {
  std::string napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
  int wynik = 3;
  assert(srednia(napis) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

