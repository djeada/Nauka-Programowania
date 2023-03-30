/*
Tytul: Slownik z kluczami bedacymi elementami jednej listy i wartosciami elementami drugiej listy.
Tresc: Dostajesz dwie listy liczb calkowitych. Stworz slownik, w ktorym kluczami beda elementy pierwszej listy, a wartosciami elementy drugiej listy. Jesli listy sa roznej dlugosci, zwroc pusty slownik.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami calkowitymi.
Przyklad:
Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], slownik powinien wygladac nastepujaco: {3: 1, 5: 2, 8: -1}.

*/
#include <cassert>
#include <unordered_map>
#include <vector>

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

