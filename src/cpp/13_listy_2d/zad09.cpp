/*
Tytul: Klepsydra o najwiekszej sumie.
Tresc: Otrzymasz liste list liczb naturalnych. Znajdz w macierzy klepsydre o najwiekszej sumie. Klepsydra sklada sie dokladnie z 7 elementow. Pierwsze trzy elementy sa kolejnymi elementami dowolnego wiersza macierzy. Czwarty element znajduje sie w tej samej kolumnie co drugi element i o jeden wiersz nizej. Ostatnie trzy elementy znajduja sie w tych samych kolumnach co trzy pierwsze i o dwa wiersze nizej.
Podpowiedz: Nastepujaca macierz:
1 2 3
4 5 6
7 8 9
ma tylko jedna klepsydre:
1 2 3
5
7 8 9
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19, 14]], powinna zostac zwrocona liczba: 75.

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

