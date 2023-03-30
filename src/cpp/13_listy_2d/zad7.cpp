/*
Tytul: Klepsydra o najwiekszej sumie.
Tresc: Otrzymasz liste list liczb naturalnych. Znajdz w macierzy klepsydre o
najwiekszej sumie. Klepsydra sklada sie dokladnie z 7 elementow. Pierwsze trzy
elementy sa kolejnymi elementami dowolnego wiersza macierzy. Czwarty element
znajduje sie w tej samej kolumnie co drugi element i o jeden wiersz nizej.
Ostatnie trzy elementy znajduja sie w tych samych kolumnach co trzy pierwsze i o
dwa wiersze nizej. Podpowiedz: Nastepujaca macierz: 1 2 3 4 5 6 7 8 9 ma tylko
jedna klepsydre: 1 2 3
5
7 8 9
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19,
14]], powinna zostac zwrocona liczba: 75.

*/
#include <cassert>
#include <vector>

void wyzerujV1(std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  if (macierz.empty())
    return;

  int M = macierz.size();
  int N = macierz[0].size();

  int wiersze[M] = {0};
  int kolumny[N] = {0};

  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (macierz[i][j] == 0) {
        wiersze[i] = 1;
        kolumny[j] = 1;
      }
    }
  }

  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      if (wiersze[i] == 1 || kolumny[j] == 1)
        macierz[i][j] = 0;
    }
  }
}

void test1() {

  std::vector<std::vector<int>> macierz{{1, 2, 3}, {4, 0, 6}, {7, 8, 9}};

  std::vector<std::vector<int>> wynik{{1, 0, 3}, {0, 0, 0}, {7, 0, 9}};

  wyzerujV1(macierz);

  assert(macierz == wynik);
}

int main() {

  test1();
  return 0;
}

