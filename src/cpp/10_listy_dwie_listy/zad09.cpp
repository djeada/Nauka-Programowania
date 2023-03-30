/*
Tytul: Usun z pierwszej listy czesc wspolna obu list.
Tresc: Otrzymujesz dwie listy liczb calkowitych. Usun z pierwszej listy te elementy, ktore wystepuja rowniez w drugiej liscie.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5].

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

