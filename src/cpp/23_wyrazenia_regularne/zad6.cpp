/*
Tytul: Cyfry w slowach.
Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa
czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete. Dane
wejsciowe: Napis. Dane wyjsciowe: Lista napisow. Przyklad: Dla otrzymanego
napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna
zostac zwrocona lista: ["29", "37", "3891", "3"].

*/

#include <cassert>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> rozdziel(const std::string &napis) {
  std::vector<std::string> wynik;
  std::string wiersz;
  std::istringstream strumien(napis);
  while (std::getline(strumien, wiersz, '\n'))
    wynik.push_back(wiersz);

  return wynik;
}

std::vector<std::string> wiersze(std::string &tekst, std::string &napis) {
  std::vector<std::string> wynik;
  std::regex wzorzec(std::string(".*" + napis + "[;,!?\\.]?"));

  auto _wiersze = rozdziel(tekst);

  for (auto &wiersz : _wiersze) {
    if (regex_match(wiersz, wzorzec))
      wynik.push_back(wiersz);
  }

  return wynik;
}

void test1() {
  std::string tekst = "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
                      "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
                      "tu cnota,\nMilosci pragna nie pragna tu zlota";
  std::string napis = "ada";
  std::vector<std::string> wynik{"Folgujmy paniom nie sobie, ma rada;",
                                 "Milujmy wiernie nie jest w nich przysada."};

  assert(wiersze(tekst, napis) == wynik);
}

int main() {

  test1();

  return 0;
}

