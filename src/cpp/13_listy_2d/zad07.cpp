/*
Tytul: Zerowanie macierzy.
Tresc: Otrzymujesz liste list liczb naturalnych reprezentujaca macierz. Jesli element macierzy jest rowny zero, zamien wszystkie elementy tej samej kolumny i wiersza na zera.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostac zwrocona macierz: [[1,0,3], [0,0,0], [7,0,9]].

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

