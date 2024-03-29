/*
Tytul: Czy napis sklada sie wylacznie z cyfr?
Tresc: Masz napis. Sprawdz, czy sklada sie on wylacznie z cyfr.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisu: “1234”, powinna zostac zwrocona wartosc logiczna: Prawda.

*/

#include <cassert>
#include <regex>
#include <string>

bool jedynieCyfry(std::string &napis) {
  std::regex wzorzec("[0-9]+");
  return regex_match(napis, wzorzec);
}

void test1() {
  std::string napis = "123542";
  assert(jedynieCyfry(napis));
}

void test2() {
  std::string napis = "2bab3";
  assert(!jedynieCyfry(napis));
}

void test3() {
  std::string napis = "124131a";
  assert(!jedynieCyfry(napis));
}

void test4() {
  std::string napis = "abc2";
  assert(!jedynieCyfry(napis));
}

int main() {

  test1();
  test2();
  test3();
  test4();

  return 0;
}

