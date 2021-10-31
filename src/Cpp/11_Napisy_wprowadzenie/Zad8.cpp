#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

/*
Otrzymujesz napis reprezentujący zdanie. Podziel zdanie na słowa składowe.
Wypisz pionowo słowa, z których składa się zdanie. Znaki interpunkcyjne
nie są liczone jako słowa.
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
