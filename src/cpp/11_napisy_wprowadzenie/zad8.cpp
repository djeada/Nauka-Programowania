#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

/*
Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe.
Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne
nie sa liczone jako slowa.
*/

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

void wypiszSlowa(std::string &napis) {
  unsigned int pocz = 0;
  unsigned int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      if (!slowo.empty())
        std::cout << slowo << std::endl;
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    if (!slowo.empty())
      std::cout << slowo << std::endl;
  }
}

int main() {
  std::string napis = "We think in generalities, but we live in details.";
  wypiszSlowa(napis);
  return 0;
}