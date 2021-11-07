#include <cassert>
#include <vector>

/*
Napisz program, realizujacy gre w statki.

Stworz macierz skladajaca sie z 10 wierszy i 10 kolumn. Wylosuj polozenia
statkow i zapisz je w macierzy. Masz do dyspozycji nastepujace statki: a) 1
statek o dlugosci rownej 4 polom, b) 2 statki o dlugosci rownej 3 polom, c) 3
statki o dlugosci rownej 2 polom, d) 5 statkow o dlugosci rownej 1 polu. Na
danym polu moze znajdowac sie tylko jeden statek.

Wypisz na standardowe wyjscie plansze skladajaca sie z 10x10 kropek i popros
uzytkownika o podanie wspolrzednych. Jesli na podanych przez uzytkownika
znajduje sie statek, zamien na planszy kropke na litere o. W przeciwnym razie
zamien kropke na litere x.

Powtarzaj krok 2 dopoki wszystkie pozycje statkow nie zostana odkryte przez
uzytkownika lub dopoki na planszy nie znajdzie sie 10 literek x. W obu
przypadkach zakoncz gre i poinformuj uzytkownika o wyniku.
*/

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
