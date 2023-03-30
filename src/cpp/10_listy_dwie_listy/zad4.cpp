/*
Tytul: Obliczenie sredniej wazonej.
Tresc: Otrzymujesz dwie listy liczb zmiennoprzecinkowych. Pierwsza lista
reprezentuje wagi, a druga wartosci. Oblicz srednia wazona. Dane wejsciowe: Dwie
listy liczb zmiennoprzecinkowych. Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2.0, 5.0, 0.0, 2.0, 1.0] oraz [0.2, 0.4, 0.1, 0.2, 0.1]
zostanie zwrocona wartosc: 0.29.

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

