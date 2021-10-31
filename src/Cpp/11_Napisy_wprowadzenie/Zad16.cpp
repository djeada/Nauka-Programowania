#include <algorithm>
#include <cassert>
#include <string>

/*
Otrzymujesz dwa napisy o równej długości. Oblicz odległość
Hamminga między dwoma otrzymanymi napisami.
*/

int odlegloscHammingaV1(const std::string &napisA, const std::string &napisB) {
  if (napisA.size() != napisB.size())
    return -1;

  int wynik = 0;

  for (unsigned int i = 0; i < napisA.size(); i++) {
    if (napisA[i] != napisB[i])
      wynik++;
  }

  return wynik;
}

void test1() {
  std::string napisA = "xxbab";
  std::string napisB = "bbabb";
  int wynik = 4;
  assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

void test2() {
  std::string napisA = "test_string";
  std::string napisB = "test_string_2";
  int wynik = -1;
  assert(odlegloscHammingaV1(napisA, napisB) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}
