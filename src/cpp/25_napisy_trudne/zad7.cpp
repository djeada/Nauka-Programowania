/*
Tytul: Powtarzajace sie podnapisy.
Tresc: Dostajesz napis. Znajdz wszystkie powtarzajace sie podnapisy w tym
napisie. Dane wejsciowe: Napis. Dane wyjsciowe: Lista napisow. Przyklad: Dla
napisu "pythonpython" powinna zostac zwrocona lista zawierajaca napis "python".

*/
#include <algorithm>
#include <cassert>
#include <string>

std::string nwp(std::string &slowoA, std::string &slowoB) {

  int N = slowoA.length() < slowoB.length() ? slowoA.length() : slowoB.length();

  for (int i = 0; i < N; i++) {
    if (slowoA[i] != slowoB[i])
      return slowoA.substr(0, i);
  }

  return slowoA.substr(0, N);
}

std::string najdluzszePowtorzenieV1(std::string &slowo) {

  std::string maks;

  int N = slowo.length();

  for (int i = 0; i < N; i++) {
    for (int j = i + 1; j < N; j++) {
      std::string slowoA = slowo.substr(i, N);
      std::string slowoB = slowo.substr(j, N);
      std::string podslowo = nwp(slowoA, slowoB);

      if (podslowo.length() > maks.length())
        maks = podslowo;
    }
  }

  return maks;
}

// Testy Poprawnosci
void test1() {
  std::string slowo = "98432934021742343230";
  std::string wynik = "432";

  assert(najdluzszePowtorzenieV1(slowo) == wynik);
}

void test2() {
  std::string slowo = "abcdef";
  std::string wynik;

  assert(najdluzszePowtorzenieV1(slowo) == wynik);
}

void test3() {
  std::string slowo = "Arnold i Arnold";
  std::string wynik = "Arnold";

  assert(najdluzszePowtorzenieV1(slowo) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

