/*
Tytul: Gra w statki
Tresc: Napisz program implementujacy gre w statki.
Stworz macierz o wymiarach 10x10. Wylosuj polozenia statkow i zapisz je w
macierzy. Do dyspozycji masz nastepujace statki:
* 1 statek o dlugosci 4
* 2 statki o dlugosci 3
* 3 statki o dlugosci 2
* 5 statkow o dlugosci 1
Kazde pole moze zawierac tylko jeden statek.
Wypisz na standardowe wyjscie plansze zlozona z 10x10 kropek i popros
uzytkownika o podanie wspolrzednych. Jesli na podanych przez uzytkownika
wspolrzednych znajduje sie statek, zamien kropke na litere o na planszy. W
przeciwnym razie, zamien kropke na litere x. Powtarzaj krok 2, az wszystkie
pozycje statkow zostana odkryte przez uzytkownika lub az na planszy pojawi sie
10 liter x. W obu przypadkach zakoncz gre i poinformuj uzytkownika o wyniku.

*/
#include <cassert>
#include <limits>
#include <vector>

int klepsydraV1(std::vector<std::vector<int>> &macierz) {
  /**
   *
   */
  int wynik = __WINT_MIN__;

  int N = macierz.size();

  for (int wiersz = 0; wiersz < N; wiersz++) {
    for (int kolumna = 0; kolumna < N; kolumna++) {
      if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1))
        wynik = std::max(
            wynik,
            (macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna] +
             macierz[wiersz - 1][kolumna + 1] + macierz[wiersz][kolumna] +
             macierz[wiersz + 1][kolumna - 1] + macierz[wiersz + 1][kolumna] +
             macierz[wiersz + 1][kolumna + 1]));
    }
  }

  return wynik;
}

void test1() {
  std::vector<std::vector<int>> macierz{{10, 99, 28, 21, 78},
                                        {35, 78, 31, 56, 24},
                                        {7, 18, 2, 50, 87},
                                        {59, 67, 9, 82, 53},
                                        {23, 26, 76, 62, 36}};

  int wynik = 395;
  assert(klepsydraV1(macierz) == wynik);
}

int main() {
  test1();
  return 0;
}

