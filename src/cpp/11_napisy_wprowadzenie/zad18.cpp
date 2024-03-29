/*
Tytul: Odwroc slowa w zdaniu.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "ala mak otak".

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc Czasowa O(n)
// Zlozonosc Pamieciowa O(1)
void odwrocNapis(std::string &slowo, int pocz, int koniec) {

  int j = koniec;

  for (int i = pocz; i <= j; i++, j--) {
    char c = slowo[i];
    slowo[i] = slowo[j];
    slowo[j] = c;
  }
}

// Zlozonosc Czasowa O(n^2)
// Zlozonosc Pamieciowa O(1)
void odwrocNapisy(std::string &zdanie) {

  unsigned int N = zdanie.length();
  unsigned int pocz = 0;
  unsigned int koniec;

  for (unsigned int i = 0; i < N; i++) {
    if (zdanie[i] == ' ' || zdanie[i] == '\0') {
      koniec = i - 1;
      odwrocNapis(zdanie, pocz, koniec);
      pocz = i + 1;
    }
  }
}

void test1() {
  std::string napis = "Cameron Diaz";
  std::string wynik = "noremaC zaiD";

  odwrocNapisy(napis);
  assert(napis == wynik);
}

int main() {

  test1();

  return 0;
}

