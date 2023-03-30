/*
Tytul: Odleglosc Hamminga.
Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga
miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch
napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych
napisy maja rozne znaki. Dane wejsciowe: Dwa napisy. Dane wyjsciowe: Liczba
naturalna. Przyklad: Dla otrzymanych napisow: “adam” i “axam”, powinna zostac
zwrocona liczba: 1.

*/
#include <algorithm>
#include <cassert>
#include <string>

void zamienV1(std::string &napis) {

  if (napis.empty())
    return;

  std::string wynik = "";

  for (int numer : napis)
    wynik += std::to_string(numer) + ", ";

  napis = wynik.substr(0, wynik.size() - 2);
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "112, 97, 99, 90, 107, 97, 33";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "";
  std::string wynik = "";

  zamienV1(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

