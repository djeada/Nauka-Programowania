#include <cassert>
#include <string>

/*
Otrzymujesz trzy napisy. Pierwszy napis reprezentuje zdanie. Drugi reprezentuje
slowo A wystepujace w zdaniu. Trzeci reprezentuje slowo B, na ktore ma zostac
zamienione slowo A. Podmien w zdaniu wszystkie wystapienia slowa A na slowo B.
*/

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
