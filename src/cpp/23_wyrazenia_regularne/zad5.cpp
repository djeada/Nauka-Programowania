/*
Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.
Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w
liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow. Dane
wejsciowe: Napis. Dane wyjsciowe: Lista napisow. Przyklad: Dla napisu: “Ani nie
poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista:
[“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

*/

#include <cassert>
#include <regex>
#include <string>

std::string odfiltrujCyfry(std::string &napis) {
  return std::regex_replace(napis, std::regex("[^0-9]*"), "");
}

void test1() {
  std::string napis = "numer 32.19 wyzej niz 31.17";
  std::string wynik = "32193117";
  assert(odfiltrujCyfry(napis) == wynik);
}

void test2() {
  std::string napis = "Lezy jerzy na wiezy";
  std::string wynik;
  assert(odfiltrujCyfry(napis) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

