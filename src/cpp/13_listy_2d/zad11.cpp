/*
Tytul: Gra w statki
Tresc: Napisz program implementujacy gre w statki.
Stworz macierz o wymiarach 10x10. Wylosuj polozenia statkow i zapisz je w macierzy. Do dyspozycji masz nastepujace statki:
* 1 statek o dlugosci 4
* 2 statki o dlugosci 3
* 3 statki o dlugosci 2
* 5 statkow o dlugosci 1
Kazde pole moze zawierac tylko jeden statek.
Wypisz na standardowe wyjscie plansze zlozona z 10x10 kropek i popros uzytkownika o podanie wspolrzednych. Jesli na podanych przez uzytkownika wspolrzednych znajduje sie statek, zamien kropke na litere o na planszy. W przeciwnym razie, zamien kropke na litere x.
Powtarzaj krok 2, az wszystkie pozycje statkow zostana odkryte przez uzytkownika lub az na planszy pojawi sie 10 liter x. W obu przypadkach zakoncz gre i poinformuj uzytkownika o wyniku.

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

