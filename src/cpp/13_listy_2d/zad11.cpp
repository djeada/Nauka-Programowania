/*
ZAD-11 — Gra w statki (projekt konsolowy)

**Poziom:** ★★★
**Tagi:** `macierze`, `losowanie`, `gra`, `pętle`

### Treść

Zaimplementuj grę w statki na planszy 10×10:

1. Plansza startowa: 10×10 wypełniona `.`
2. Losowo rozmieść statki (poziomo/pionowo), bez stykania bokami ani rogami:

   * 1× długość 4
   * 2× długość 3
   * 3× długość 2
   * 5× długość 1
3. Pętla gry:

   * wypisz planszę,
   * wczytaj `r c` (0..9),
   * jeśli trafienie: wstaw `o`, wypisz komunikat o trafieniu,
   * jeśli pudło: wstaw `x`, zwiększ licznik pudeł,
   * gra kończy się, gdy:

     * wszystkie pola statków trafione (wygrana), albo
     * 10 pudeł (przegrana).
   * po każdym ruchu wypisz zaktualizowaną planszę.

### Wejście

Wielokrotnie:

* `r c` (w jednej linii)

### Wyjście

* plansza i komunikaty w trakcie,
* na końcu komunikat o wygranej/przegranej.

### Uwagi praktyczne

* To zadanie jest **większym projektem** — format wyjścia bywa sprawdzany
„ręcznie” (nie zawsze automatycznie), więc trzymaj się spójnego stylu
wypisywania planszy.

*/
#include <cassert>
#include <vector>

// Zlozonosc Czasowa: O(n^2)
// Zlozonosc Pamieciowa: O(1)
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
