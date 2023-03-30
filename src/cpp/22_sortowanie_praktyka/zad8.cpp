/*
Tytul: Wyszukiwanie indeksu klucza w cyklicznie posortowanej liscie.
Tresc: Otrzymujesz cyklicznie posortowana liste oraz klucz. Znajdz indeks
pierwszego wystapienia klucza w liscie. Jesli klucz nie wystepuje w liscie,
zwroc -1. Dane wejsciowe: Cyklicznie posortowana lista, klucz. Dane wyjsciowe:
Indeks pierwszego wystapienia klucza lub -1. Przyklad: Dla cyklicznie
posortowanej listy [3, 4, 5, 6, 1, 2] i klucza 4, powinno zostac zwrocone 2.

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Otrzymuejsz cyklicznie posortowana liste oraz klucz.
// Znajdz indeks pierwszego wystapienia klucza w liscie.
// Jesli klucz nie wystepuje w liscie zwroc -1.

int znajdzKlucz(std::vector<int> &lista, int klucz) {
  int lewo = 0;
  int prawo = lista.size() - 1;

  while (lewo <= prawo) {

    auto sr = (lewo + prawo) / 2;

    if (klucz == lista[sr])
      return sr;

    if (lista[sr] <= lista[prawo]) {

      if (lista[sr] < klucz && klucz <= lista[prawo])
        lewo = sr + 1;

      else
        prawo = sr - 1;
    }

    else {

      if (lista[lewo] <= klucz && klucz < lista[sr])
        prawo = sr - 1;

      else
        lewo = sr + 1;
    }
  }

  return -1;
}

void test1() {
  std::vector<int> lista{27, 31, 32, 3, 5, 9, 10, 15};
  int klucz = 31;
  int wynik = 1;

  assert(znajdzKlucz(lista, klucz) == wynik);
}

void test2() {
  std::vector<int> lista{4, 7, 12, 32, 51, 90, 100, 1, 2};
  int klucz = -5;
  int wynik = -1;

  assert(znajdzKlucz(lista, klucz) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

