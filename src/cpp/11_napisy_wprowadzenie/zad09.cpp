/*
Tytul: Wczytaj i rozdziel informacje o pracowniku.
Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",
powinna zostac zwrocona lista:
["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod: Programista", "Zarobki: 1000"].

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

