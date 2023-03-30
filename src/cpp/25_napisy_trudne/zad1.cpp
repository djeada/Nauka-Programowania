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

std::string zamienWszystkoV1(std::string zdanie, std::string napisA,
                             std::string napisB) {

  auto k = zdanie.find(napisA);

  while (k != std::string::npos) {
    zdanie.replace(k, napisA.size(), napisB);
    k = zdanie.find(napisA, k + napisB.size());
  }

  return zdanie;
}

// Testy Poprawnosci
void test1() {
  std::string zdanie = "Lezy jezy na wiezy";
  std::string napisA = "zy";
  std::string napisB = "rzy";
  std::string wynik = "Lerzy jerzy na wierzy";

  assert(zamienWszystkoV1(zdanie, napisA, napisB) == wynik);
}

int main() {

  test1();

  return 0;
}

// Compiled with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe

