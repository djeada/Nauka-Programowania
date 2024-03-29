/*
Tytul: Minimum oraz maksimum.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy element tej listy i zwroc je jako dwie osobne liczby calkowite.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Dwie liczby calkowite oznaczajace najwiekszy i najmniejszy element z listy.
Przyklad:
Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.

*/
#include <algorithm>
#include <cassert>
#include <limits>
#include <vector>

int maksV1(std::vector<int> &lista) {

  if (lista.empty())
    return std::numeric_limits<int>::min();

  int maks = lista.front();

  for (auto liczba : lista) {
    if (liczba > maks)
      maks = liczba;
  }

  return maks;
}

int minV1(std::vector<int> &lista) {

  if (lista.empty())
    return std::numeric_limits<int>::max();

  int min = lista.front();

  for (auto liczba : lista) {
    if (liczba < min)
      min = liczba;
  }

  return min;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};

  assert(maksV1(lista) == *std::max_element(lista.begin(), lista.end()));
  assert(minV1(lista) == *std::min_element(lista.begin(), lista.end()));
}

void test2() {
  std::vector<int> lista{3, -2, 4, 29, -3, -40, 8, 5, -7, -1};

  assert(maksV1(lista) == *std::max_element(lista.begin(), lista.end()));
  assert(minV1(lista) == *std::min_element(lista.begin(), lista.end()));
}

int main() {

  test1();
  test2();

  return 0;
}

