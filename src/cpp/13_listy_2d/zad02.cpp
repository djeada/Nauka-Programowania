/*
Tytul: Macierz kwadratowa, z elementami bedacymi iloczynem wspolrzednych.
Tresc: Dla otrzymanej liczby naturalnej n, stworz macierz kwadratowa o rozmiarze n x n, ktorej kazdy element jest iloczynem jego wspolrzednych.
Dane wejsciowe: Liczba naturalna n.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej liczby 3 powinna zostac zwrocona macierz: [[0, 0, 0], [0, 1, 2], [0, 2, 4]].

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

