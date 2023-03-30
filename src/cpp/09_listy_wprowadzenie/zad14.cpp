/*
Tytul: Czy srednia elementow znajduje sie w liscie?
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako
klucza, usun pierwsze wystapienie klucza w liscie. Dane wejsciowe: Lista liczb
calkowitych i liczba calkowita jako klucz. Dane wyjsciowe: Lista liczb
calkowitych bez pierwszego wystapienia klucza. Przyklad: Dla otrzymanej listy
[6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

*/
#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int elementBezParyV1(std::vector<int> &lista) {
  std::vector<int> pom;

  for (auto liczba : lista) {
    auto i = find(pom.begin(), pom.end(), liczba);
    if (i != pom.end())
      pom.erase(i);
    else
      pom.push_back(liczba);
  }

  return pom.front();
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int elementBezParyV2(std::vector<int> &lista) {
  int wynik = 0;

  for (auto liczba : lista)
    wynik ^= liczba;

  return wynik;
}

void test1() {
  std::vector<int> lista{1, 3, 1, 7, 3, 1, 1};
  int wynik = 7;
  assert(elementBezParyV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 3, 1, 7, 3, 1, 1};
  int wynik = 7;
  assert(elementBezParyV2(lista) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

