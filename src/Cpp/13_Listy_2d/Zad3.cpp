#include <cassert>
#include <utility>
#include <vector>

/*
Dla otrzymanych dwóch list, stwórz dwukolumnową macierz, której pierwsza 
kolumna składa się z elementów pierwszej listy, a druga kolumna elementów 
drugiej listy. Jeśli otrzymane listy nie są równej długości zwróć pustą macierz.
*/

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
