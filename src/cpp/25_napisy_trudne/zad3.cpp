/*
Tytul: Usun podnapis.
Tresc: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usuniecie
wszystkich wystapien drugiego napisu w pierwszym napisie. Dane wejsciowe: Dwa
napisy. Dane wyjsciowe: Napis. Przyklad: Dla napisow: “Lezy jezy na wiezy” oraz
“zy”, zwrocony napis powinien brzmiec: “Le je na wie”.

*/
#include <algorithm>
#include <cassert>
#include <string>

bool jednakowyPoczatekV1(string slowoA, string slowoB) {
  transform(slowoA.begin(), slowoA.end(), slowoA.begin(), ::tolower);
  transform(slowoB.begin(), slowoB.end(), slowoB.begin(), ::tolower);

  return !slowoA.find(slowoB);
}

// Testy Poprawnosci
void test1() {
  std::string slowoA = "Dinozaur jest zly";
  std::string slowoB = "Dino";

  assert(jednakowyPoczatekV1(slowoA, slowoB));
}

void test2() {
  std::string slowoA = "Dinozaur jest zly";
  std::string slowoB = "Pies";

  assert(!jednakowyPoczatekV1(slowoA, slowoB));
}

int main() {

  test1();
  test2();

  return 0;
}

