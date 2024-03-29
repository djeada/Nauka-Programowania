/*
Tytul: Znalezienie brakujacego elementu w liscie.
Tresc: Dla dostarczonej listy, skladajacej sie z nieuporzadkowanych kolejnych (oprocz jednego) elementow ciagu arytmetycznego, znajdz brakujacy element.
Dane wejsciowe: Lista zawierajaca liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrocona liczba: 4.

*/
#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

int sumaCiaguArt(std::vector<int> &lista) {
  int min = *min_element(lista.begin(), lista.end());
  int maks = *max_element(lista.begin(), lista.end());
  return (lista.size() + 1) * (min + maks) / 2;
}

int znajdzBrakujacyElement(std::vector<int> &lista) {

  int sumaListy = accumulate(lista.begin(), lista.end(), 0);
  int sumaPrzedzialu = sumaCiaguArt(lista);

  return sumaPrzedzialu - sumaListy;
}

void test1() {
  std::vector<int> lista{6, 8, 4, 10, 14, 2};
  int wynik = 12;
  assert(znajdzBrakujacyElement(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 2, 4, 5, 6};
  int wynik = 3;
  assert(znajdzBrakujacyElement(lista) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

