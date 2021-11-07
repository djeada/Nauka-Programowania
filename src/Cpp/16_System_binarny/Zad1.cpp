#include <cassert>
#include <cmath>
#include <string>

/*
a) Otrzymujesz dziesietna reprezentacje liczby naturalnej, zwroc jej binarna
reprezentacje. b) Otrzymujesz binarna reprezentacje liczby naturalnej, zwroc jej
dziesietna reprezentacje.
*/

int naDziesietny(std::string liczba) {
  /*
   * Funkcja zamienia liczbe binarna na dziesietna.
   */
  auto naLiczbe = [](char c) { return c - '0'; };

  int dec = 0;
  int n = liczba.size();
  for (int i = 0; i < n; i++)
    dec += pow(2, n - i - 1) * naLiczbe(liczba[i]);

  return dec;
}

std::string naBinarny(int liczba) {
  /*
   * Funkcja zamienia liczbe dziesietna na binarna.
   */
  std::string bin;

  while (liczba > 0) {
    bin.insert(0, std::to_string(liczba % 2));
    liczba /= 2;
  }

  return bin;
}

void test1() {
  std::string liczba = "0011";
  int wynik = 3;

  assert(naDziesietny(liczba) == wynik);
}

void test2() {
  std::string liczba = "1111100";
  int wynik = 124;

  assert(naDziesietny(liczba) == wynik);
}

void test3() {
  int liczba = 124;
  std::string wynik = "1111100";

  assert(naBinarny(liczba) == wynik);
}

void test4() {
  int liczba = 3;
  std::string wynik = "11";

  assert(naBinarny(liczba) == wynik);
}

int main() {

  test1();
  test2();
  test3();
  test4();

  return 0;
}
