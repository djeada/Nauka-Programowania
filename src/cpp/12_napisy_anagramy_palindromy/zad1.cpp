/*
Tytul: Sprawdzenie, czy slowo jest palindromem.
Tresc: Napisz program, ktory sprawdzi, czy slowo jest palindromem. Palindromem
jest slowo, ktore brzmi tak samo czytane od lewej do prawej i od prawej do
lewej. Dane wejsciowe: Napis. Dane wyjsciowe: Wartosc logiczna. Przyklad: Dla
otrzymanego napisu: “kajak”, powinna zostac zwrocona wartosc logiczna: Prawda.

*/
#include <algorithm>
#include <cassert>
#include <string>

bool palindrom(std::string &slowo) {
  int N = slowo.length() - 1;
  for (int i = 0; i <= N / 2; i++) {
    if (slowo[i] != slowo[N - i])
      return false;
  }

  return true;
}

void test1() {
  std::string slowo = "kajak";
  assert(palindrom(slowo));
}

void test2() {
  std::string slowo = "Pan";
  assert(!palindrom(slowo));
}

int main() {

  test1();
  test2();

  return 0;
}

