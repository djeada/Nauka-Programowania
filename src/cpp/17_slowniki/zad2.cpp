#include <cassert>
#include <unordered_map>
#include <vector>

/*
Otrzymujesz dwie listy liczb calkowitych. Zbuduj slownik skladajacy sie z
kluczy bedacych elementami pierwszej listy i wartosciami bedacymi elementami
drugiej listy. Jesli listy sa roznej dlugosci zwroc pusty slownik.
*/

std::unordered_map<int, int> budujSlownik(std::vector<int> &listaA,
                                          std::vector<int> &listaB) {
  /*
   * Funkcja tworzy slownik zawierajacy klucze bedace elementami
   * pierwszej listy i wartosci bedace elementami drugiej listy.
   */
  std::unordered_map<int, int> slownik;

  if (listaA.size() != listaB.size())
    return slownik;

  for (unsigned int i = 0; i < listaA.size(); i++)
    slownik[listaA[i]] = listaB[i];

  return slownik;
}

void test1() {
  std::vector<int> listaA{3, 5, 8};
  std::vector<int> listaB{1, 2, -1};
  std::unordered_map<int, int> wynik{{3, 1}, {5, 2}, {8, -1}};

  assert(budujSlownik(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{0, 1};
  std::vector<int> listaB{1, 0};
  std::unordered_map<int, int> wynik{{0, 1}, {1, 0}};

  assert(budujSlownik(listaA, listaB) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}
