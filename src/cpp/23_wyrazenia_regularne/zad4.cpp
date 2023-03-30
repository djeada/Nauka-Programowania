/*
Tytul: Wiersze konczace sie okreslonym napisem.
Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie
drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.
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
powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy
wiernie nie jest w nich przysada.”]

*/

#include <cassert>
#include <regex>
#include <string>

bool nalezyDoZdania(std::string &zdanie, std::string &napis) {
  return regex_search(zdanie, std::regex(napis));
}

void test1() {
  std::string zdanie = "Mozart gra na skrzypcach";
  std::string napis = "skrzyp";
  assert(nalezyDoZdania(zdanie, napis));
}

void test2() {
  std::string zdanie = "Lezy jerzy na wiezy";
  std::string napis = "nan";
  assert(!nalezyDoZdania(zdanie, napis));
}

int main() {

  test1();
  test2();

  return 0;
}

