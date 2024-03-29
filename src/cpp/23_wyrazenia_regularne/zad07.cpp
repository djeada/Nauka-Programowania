/*
Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.
Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

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

