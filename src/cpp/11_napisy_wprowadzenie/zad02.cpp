/*
Tytul: Policz wystapienia znaku.
Tresc: Dla podanego napisu i znaku, znajdz liczbe wystapien tego znaku w napisie.
Dane wejsciowe: Napis oraz znak.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostac zwrocone: 2.

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa O(n)
// Zlozonosc Pamieciowa O(1)
int policzZnakV1(const std::string &slowo, const char &znak) {

  int licznik = 0;

  for (auto x : slowo) {
    if (x == znak)
      licznik++;
  }

  return licznik;
}

void test1() {
  std::string napis = "adam";
  char znak = 'a';
  int wynik = 2;

  assert(policzZnakV1(napis, znak) == wynik);
}

int main() {
  test1();
  return 0;
}

