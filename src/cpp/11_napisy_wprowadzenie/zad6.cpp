/*
Tytul: Slowa ze zdania jako osobne elementy listy.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zwroc liste slow zdania. Znaki
interpunkcyjne nie sa liczone jako slowa. Dane wejsciowe: Napis. Dane wyjsciowe:
Lista napisow. Przyklad: Dla otrzymanego napisu: “Ala ma kota”, powinna zostac
zwrocona lista: [“Ala”, “ma”, “kota”].

*/
#include <algorithm>
#include <cassert>
#include <string>

void zamienV1(std::string &napis) {

  for (auto &znak : napis) {
    if (znak == 'a')
      znak = '?';
  }
}

void zamienV2(std::string &napis) {
  replace(napis.begin(), napis.end(), 'a', '?');
}

void test1() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV1(napis);
  assert(napis == wynik);
}

void test2() {
  std::string napis = "pacZka!";
  std::string wynik = "p?cZk?!";

  zamienV2(napis);
  assert(napis == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

