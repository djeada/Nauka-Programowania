/*
Tytul: Podmiana slowa w zdaniu.
Tresc: Masz trzy napisy: zdanie, slowo A i slowo B. Twoim zadaniem jest zamiana
wszystkich wystapien slowa A na slowo B w zdaniu. Dane wejsciowe: Trzy napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrocony napis powinien
brzmiec: “Lerzy jerzy na wierzy”.

*/
#include <cassert>
#include <string>

std::string usunWszystkieV1(std::string zdanie, const std::string &slowo) {
  auto k = zdanie.find(slowo);

  while (k != string::npos) {
    zdanie.erase(k, slowo.length());
    k = zdanie.find(slowo);
  }

  return zdanie;
}

// Testy Poprawnosci
void test1() {
  std::string zdanie = "Lezy jezy na wiezy";
  std::string slowo = "zy";
  std::string wynik = "Le je na wie";

  assert(usunWszystkieV1(zdanie, slowo) == wynik);
}

int main() {

  test1();

  return 0;
}

