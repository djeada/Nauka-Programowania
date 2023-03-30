/*
Tytul: Usun fragment napisu.
Tresc: Dostajesz dwa napisy. Pierwszy napis to tekst, a drugi to slowo, ktore
nalezy usunac z tekstu. Jesli w tekscie znajduje sie slowo do usuniecia, usun
cala czesc tekstu od slowa do konca. Zwroc zmodyfikowany tekst. Dane wejsciowe:
Dwa napisy. Dane wyjsciowe: Napis. Przyklad: Dla podanych napisow: > Turned it
up should no valley cousin he. Speaking numerous ask did horrible packages set.
Ashamed herself has distant can studied mrs.
Led therefore its middleton perpetual fulfilled provision frankness.
Small he drawn after among every three no.
All having but you edward genius though remark one.
Rooms oh fully taken by worse do.
Points afraid but may end law lasted.
Was out laughter raptures returned outweigh.
Luckily cheered colonel me do we attacks on highest enabled.
Tried law yet style child.
Bore of true of no be deal.
Frequently sufficient in be unaffected.
The furnished she concluded depending procuring concealed.
oraz slowa "a", powinien zostac zwrocony napis:
> Turned it up should no v
Spe
Ash
Led therefore its middleton perpetu
Sm
All h
Rooms oh fully t
Points
W
Luckily cheered colonel me do we
Tried l
Bore of true of no be de
Frequently sufficient in be un
The furnished she concluded depending procuring conce.

*/

#include <cassert>
#include <regex>
#include <string>
#include <vector>

std::string przytnijLewo(const std::string &napis) {
  return std::regex_replace(napis, std::regex("^\\s+"), std::string(""));
}

std::string przytnijPrawo(const std::string &napis) {
  return std::regex_replace(napis, std::regex("\\s+$"), std::string(""));
}

std::string przytnij(const std::string &napis) {
  return przytnijLewo(przytnijPrawo(napis));
}

std::vector<std::string> rozdziel(const std::string &napis) {
  std::vector<std::string> wynik;
  std::regex wzorzec("[,;!?\\.]");
  std::sregex_token_iterator it(napis.begin(), napis.end(), wzorzec, -1);

  for (std::sregex_token_iterator koniec; it != koniec; ++it)
    wynik.push_back(przytnij(*it));

  return wynik;
}

void test1() {
  std::string napis = "Ani nie poszedl do kina, ani nie wybral sie do teatru.";
  std::vector<std::string> wynik{"Ani nie poszedl do kina",
                                 "ani nie wybral sie do teatru"};

  assert(rozdziel(napis) == wynik);
}

int main() {

  test1();

  return 0;
}

