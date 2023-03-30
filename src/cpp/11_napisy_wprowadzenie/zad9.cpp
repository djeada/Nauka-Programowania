/*
Tytul: Odwroc slowa w zdaniu.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same
napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa. Dane
wejsciowe: Napis. Dane wyjsciowe: Napis. Przyklad: Dla otrzymanego napisu: "Ala
ma kota", powinien zostac zwrocony napis: "ala mak otak".

*/
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>

std::vector<std::string> dane(std::string &napis) {

  std::vector<std::string> wynik;
  std::stringstream ss(napis);

  for (std::string slowo; ss >> slowo;) {
    if (slowo.size() > 1) {
      wynik.push_back(slowo.substr(0, slowo.size() - 1));
      if (ss.peek() == ';')
        ss.ignore();
    }
  }

  return wynik;
}

void wypiszDane(std::string &napis) {

  std::vector<std::string> wynik = dane(napis);
  assert(wynik.size() == 5);

  std::cout << "Imie: " << wynik[0] << std::endl;
  std::cout << "Nazwisko: " << wynik[1] << std::endl;
  std::cout << "Miejsce urodzenia: " << wynik[2] << std::endl;
  std::cout << "Zawod: " << wynik[3] << std::endl;
  std::cout << "Zarobki: " << wynik[4] << std::endl;
}

int main() {
  std::string napis = "Jan; Kowalski; Warszawa; Programista; 1000";
  wypiszDane(napis);
  return 0;
}

