/*
Tytul: Mnozenie wektorowe.
Tresc: Tresc: Otrzymujesz dwie listy liczb calkowitych reprezentujace dwa wektory trojwymiarowej przestrzeni euklidesowej. Zaimplementuj mnozenie wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni euklidesowej).
Dane wejsciowe: Dwie listy liczb calkowitych o dlugosci 3.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych list [1, 2, 3] oraz [3, 1, 2], powinno zostac zwrocone: 5.

*/
#include <cassert>
#include <vector>

std::vector<int> mnozenieWektorowe(std::vector<int> &listaA,
                                   std::vector<int> &listaB) {

  assert(listaA.size() == listaB.size() && listaA.size() == 3);

  std::vector<int> wynik;
  wynik.push_back(listaA[1] * listaB[2] - listaA[2] * listaB[1]);
  wynik.push_back(listaA[2] * listaB[0] - listaA[0] * listaB[2]);
  wynik.push_back(listaA[0] * listaB[1] - listaA[1] * listaB[0]);

  return wynik;
}

void testMnozenieWektorowe() {
  std::vector<int> listaA{3, -5, 4};
  std::vector<int> listaB{2, 6, 5};

  std::vector<int> iloczynWekt({-49, -7, 28});
  assert(mnozenieWektorowe(listaA, listaB) == iloczynWekt);
}

int main() {

  testMnozenieWektorowe();

  return 0;
}

