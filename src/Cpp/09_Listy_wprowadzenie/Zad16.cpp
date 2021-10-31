#include <algorithm>
#include <cassert>
#include <vector>

/*
Dla otrzymanej listy oraz liczby x, znajdź indeksy pierwszej pary 
elementów listy, których suma jest równa liczbie x. Jeśli w liście 
nie ma takiej pary, zwróć parę (-1, -1).
*/

std::vector<std::pair<int, int>> znajdzParyV1(std::vector<int> &lista,
                                              int suma) {

  std::vector<std::pair<int, int>> wynik;

  for (unsigned int i = 0; i < lista.size(); i++) {
    for (unsigned int j = i + 1; j < lista.size(); j++) {
      if (lista[i] + lista[j] == suma)
        wynik.emplace_back(lista[i], lista[j]);
    }
  }

  return wynik;
}

void test1() {
  std::vector<int> lista{0, 4, 5, 6, 2, 9, 2, 3};
  std::vector<std::pair<int, int>> wynik{{0, 5}, {2, 3}, {2, 3}};
  int suma = 5;

  assert(znajdzParyV1(lista, suma) == wynik);
}

int main() {

  test1();

  return 0;
}
