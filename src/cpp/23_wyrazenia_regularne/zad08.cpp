/*
Tytul: Cyfry w slowach.
Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna zostac zwrocona lista: ["29", "37", "3891", "3"].

*/

#include <cassert>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> cyfry(const std::string &napis) {
  std::string slowo;
  std::stringstream ss(napis);

  std::vector<std::string> wynik;

  while (ss >> slowo) {
    if (std::regex_search(slowo, std::regex("[0-9]+")) &&
        std::regex_search(slowo, std::regex("[^0-9]+")))
      wynik.push_back(std::regex_replace(slowo, std::regex("[^0-9]*"), ""));
  }

  return wynik;
}

void test1() {
  std::string napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
  std::vector<std::string> wynik{"29", "37", "3891", "3"};

  assert(cyfry(napis) == wynik);
}

int main() {

  test1();

  return 0;
}

