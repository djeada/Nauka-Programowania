#include <cassert>
#include <vector>

/*
Napisz program, realizujący grę w statki. 

Stwórz macierz składającą się z 10 wierszy i 10 kolumn. Wylosuj położenia statków 
i zapisz je w macierzy. Masz do dyspozycji następujące statki: 
a) 1 statek o długości równej 4 polom, 
b) 2 statki o długości równej 3 polom, 
c) 3 statki o długości równej 2 polom, 
d) 5 statków o długości równej 1 polu. 
Na danym polu może znajdować się tylko jeden statek.

Wypisz na standardowe wyjście planszę składającą się z 10x10 kropek i poproś 
użytkownika o podanie współrzędnych. Jeśli na podanych przez użytkownika znajduje 
się statek, zamień na planszy kropkę na literę o. W przeciwnym razie zamień 
kropkę na literę x.

Powtarzaj krok 2 dopóki wszystkie pozycje statków nie zostaną odkryte przez 
użytkownika lub dopóki na planszy nie znajdzie się 10 literek x. W obu 
przypadkach zakończ grę i poinformuj użytkownika o wyniku.
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
