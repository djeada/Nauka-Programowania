/*
Tytul: Sprawdz czy slowo wystepuje w zdaniu.
Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

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

