/*
Tytul: Sprawdzanie czy macierz jest "magiczna".
Tresc: Otrzymujesz macierz kwadratowa. Sprawdz, czy jest ona kwadratem
magicznym. Podpowiedz: Kwadrat magiczny sklada sie z powtarzajacych sie
dodatnich liczb naturalnych. Suma elementow w kazdym wierszu, w kazdej kolumnie
oraz na kazdej przekatnej jest taka sama. Dane wejsciowe: Lista list liczb
naturalnych. Dane wyjsciowe: Wartosc logiczna. Przyklad: Dla otrzymanej
macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostac zwrocona wartosc
logiczna: Prawda.

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::pair<int, int>> macierz(std::vector<int> listaA,
                                         std::vector<int> listaB) {
  /**
   *
   */
  std::vector<std::pair<int, int>> macierz;

  if (listaA.size() != listaB.size())
    return macierz;

  int n = listaA.size();
  macierz.reserve(n);

  for (int i = 0; i < n; i++)
    macierz.push_back(std::pair<int, int>(listaA[i], listaB[i]));

  return macierz;
}

void test1() {
  std::vector<std::pair<int, int>> wynik{{3, 2}, {5, 8}, {2, 1}};
  std::vector<int> listaA{3, 5, 2};
  std::vector<int> listaB{2, 8, 1};
  assert(macierz(listaA, listaB) == wynik);
}

int main() {
  test1();
  return 0;
}

