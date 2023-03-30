/*
Tytul: Scalanie przedzialow w liscie przedzialow.
Tresc: Otrzymujesz liste par liczb. Kazda para reprezentuje poczatek i koniec
przedzialu. Niektore przedzialy moga sie nachodzic. W takim przypadku polacz je
ze soba i zwroc liste przedzialow, ktore sie nie pokrywaja. Dane wejsciowe:
Lista list liczb naturalnych. Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej listy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11,
12], [42, 45]], powinna zostac zwrocona lista: [[10, 22], [23, 88]].

*/
#include <cassert>
#include <vector>

bool wymiaryRowne(std::vector<std::vector<int>> macierzA,
                  std::vector<std::vector<int>> macierzB) {
  /**
   *
   */
  if (macierzA.size() != macierzB.size())
    return false;

  for (unsigned int i = 0; i < macierzA.size(); i++) {
    if (macierzA[i].size() != macierzB[i].size())
      return false;
  }

  return true;
}

std::vector<std::vector<int>> dodaj(std::vector<std::vector<int>> macierzA,
                                    std::vector<std::vector<int>> macierzB) {
  /**
   *
   */
  std::vector<std::vector<int>> wynik;

  if (!wymiaryRowne(macierzA, macierzB))
    return wynik;

  for (unsigned int i = 0; i < macierzA.size(); ++i) {
    std::vector<int> wiersz;
    for (unsigned int j = 0; j < macierzA[i].size(); ++j)
      wiersz.push_back(macierzA[i][j] + macierzB[i][j]);
    wynik.push_back(wiersz);
  }

  return wynik;
}

std::vector<std::vector<int>> odejmij(std::vector<std::vector<int>> macierzA,
                                      std::vector<std::vector<int>> macierzB) {
  /**
   *
   */
  std::vector<std::vector<int>> wynik;

  if (!wymiaryRowne(macierzA, macierzB))
    return wynik;

  for (unsigned int i = 0; i < macierzA.size(); ++i) {
    std::vector<int> wiersz;
    for (unsigned int j = 0; j < macierzA[i].size(); ++j)
      wiersz.push_back(macierzA[i][j] - macierzB[i][j]);
    wynik.push_back(wiersz);
  }

  return wynik;
}

void test1() {
  std::vector<std::vector<int>> macierzA{{1, 2}, {-2, 0}};
  std::vector<std::vector<int>> macierzB{{5, -3}, {1, 7}};
  std::vector<std::vector<int>> wynik{{6, -1}, {-1, 7}};
  assert(dodaj(macierzA, macierzB) == wynik);
}

void test2() {
  std::vector<std::vector<int>> macierzA{{1, 2}, {-2, 0}};
  std::vector<std::vector<int>> macierzB{{5, -3}, {1, 7}};
  std::vector<std::vector<int>> wynik{{-4, 5}, {-3, -7}};
  assert(odejmij(macierzA, macierzB) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

