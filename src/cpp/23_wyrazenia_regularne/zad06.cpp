/*
Tytul: Wiersze konczace sie okreslonym napisem.
Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisow:
> Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota.
oraz
> da
powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

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

