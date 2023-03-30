/*
Tytul: Macierz z parami elementow odpowiadajacych sobie z dwoch list.
Tresc: Dla otrzymanych dwoch list, stworz dwukolumnowa macierz, ktorej pierwsza
kolumna sklada sie z elementow pierwszej listy, a druga kolumna z elementow
drugiej listy. Jesli otrzymane listy nie sa rownej dlugosci, zwroc pusta
macierz. Dane wejsciowe: Dwie listy. Dane wyjsciowe: Lista list liczb
naturalnych lub pusta macierz (w przypadku nierownych dlugosci list). Przyklad:
Dla otrzymanych dwoch list: [3, 5, 2] oraz [2, 8, 1], powinna zostac zwrocona
macierz: [[3, 2], [5, 8], [2, 1]

*/
#include <cassert>
#include <vector>

void obroc(std::vector<std::vector<int>> &macierz) {

  int N = macierz.size();

  for (int i = 0; i < N / 2; i++) {
    int first = i + 1;
    int last = N - 1 - i;

    for (int j = first; j < last; j++) {
      int pom = macierz[i][j];
      macierz[i][j] = macierz[N - 1 - j][i];
      macierz[N - 1 - j][i] = macierz[N - 1 - i][N - 1 - j];
      macierz[N - 1 - i][N - 1 - j] = macierz[j][N - 1 - i];
      macierz[j][N - 1 - i] = pom;
    }

    int pom = macierz[i][i];
    macierz[i][i] = macierz[N - 1 - i][i];
    macierz[N - 1 - i][i] = macierz[N - 1 - i][N - 1 - i];
    macierz[N - 1 - i][N - 1 - i] = macierz[i][N - 1 - i];
    macierz[i][N - 1 - i] = pom;
  }
}

void test1() {
  std::vector<std::vector<int>> macierz{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  std::vector<std::vector<int>> wynik{{7, 4, 1}, {8, 5, 2}, {9, 6, 3}};

  obroc(macierz);
  assert(macierz == wynik);
}

int main() {

  test1();

  return 0;
}

