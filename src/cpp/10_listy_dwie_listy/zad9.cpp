/*
Tytul: Znajdz mediane dwoch posortowanych list.
Tresc: Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci.
Znajdz ich mediane. Dane wejsciowe: Dwie listy liczb calkowitych o rownej
dlugosci. Dane wyjsciowe: Liczba zmiennoprzecinkowa. Przyklad: Dla otrzymanych
list [2, 4, 7] oraz [3, 5, 9] powinno zostac zwrocone: 4.5.

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Zlozonosc obliczeniowa O(n^2)
// Zlozonosc pamieciowa O(n)
void usunCzescWspolnaV1(std::vector<int> &listaA, std::vector<int> &listaB) {

  auto it = listaA.begin();

  while (it != listaA.end()) {
    if (find(listaB.begin(), listaB.end(), *it) != listaB.end())
      it = listaA.erase(it);
    else
      it++;
  }
}

void test1() {
  std::vector<int> listaA{3, 6, 2, 7, 9};
  std::vector<int> listaB{4, 2, 3, 5, 6};
  std::vector<int> wynik{7, 9};

  usunCzescWspolnaV1(listaA, listaB);

  assert(listaA == wynik);
}

int main() {

  test1();

  return 0;
}

