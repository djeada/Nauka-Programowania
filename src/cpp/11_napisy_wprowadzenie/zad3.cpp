/*
Tytul: Usun spacje ze zdania.
Tresc: Otrzymasz napis reprezentujacy zdanie. Usun spacje ze zdania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis:
"Alamakota".

*/
#include <algorithm>
#include <cassert>
#include <string>

// Zlozonosc Czasowa O(n)
// Zlozonosc Pamieciowa O(1)
int policzSlowaV1(std::string &slowo) {

  bool spacja = true;
  int licznik = 0;

  for (auto znak : slowo) {
    if (isspace(znak))
      spacja = true;
    else if (isalpha(znak) && spacja) {
      licznik++;
      spacja = false;
    }
  }

  return licznik;
}

void test1() {
  std::string napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
  int wynik = 9;

  assert(policzSlowaV1(napis) == wynik);
}

int main() {
  test1();
  return 0;
}

