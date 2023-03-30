/*
Tytul: Dodawanie i odejmowanie macierzy.
Tresc: Otrzymujesz dwie macierze o tych samych wymiarach. Zwroc dwie macierze
bedace: a) wynikiem dodawania otrzymanych macierzy b) wynikiem odejmowania
drugiej macierzy od pierwszej. Dane wejsciowe: Dwie listy list liczb
naturalnych. Dane wyjsciowe: Dwie listy list liczb naturalnych. Przyklad: Dla
otrzymanych dwoch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinny
zostac zwrocone nastepujace macierze: a) [[6, -1], [-1, 7]] - wynik dodawania b)
[[-4, 5], [-3, -7]] - wynik odejmowania drugiej macierzy od pierwszej.

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::vector<int>> macierz(int n) {
  /**
   *
   */
  std::vector<std::vector<int>> macierz;
  macierz.reserve(n);

  for (int i = 0; i < n; i++) {
    std::vector<int> wiersz;
    for (int j = 0; j < n; j++)
      wiersz.push_back(i * j);
    macierz.push_back(wiersz);
  }

  return macierz;
}

void test1() {
  int n = 4;
  std::vector<std::vector<int>> wynik{
      {0, 0, 0, 0}, {0, 1, 2, 3}, {0, 2, 4, 6}, {0, 3, 6, 9}};
  assert(macierz(n) == wynik);
}

int main() {
  test1();
  return 0;
}

