/*
Tytul: Usun z pierwszej listy czesc wspolna obu list.
Tresc: Otrzymujesz dwie listy liczb calkowitych. Usun z pierwszej listy te
elementy, ktore wystepuja rowniez w drugiej liscie. Dane wejsciowe: Dwie listy
liczb calkowitych. Dane wyjsciowe: Lista liczb calkowitych. Przyklad: Dla
otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9,
5].

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Zlozonosc obliczeniowa O(n)
// Zlozonosc pamieciowa O(n)
std::vector<int> polaczV1(std::vector<int> &listaA, std::vector<int> &listaB) {

  if (listaA.empty())
    return listaB;

  if (listaB.empty())
    return listaA;

  std::vector<int> wynik;

  unsigned int i = 0;
  unsigned int j = 0;

  while (i < listaA.size() && j < listaB.size()) {
    if (listaA[i] < listaB[j]) {
      wynik.push_back(listaA[i]);
      i++;
    } else {
      wynik.push_back(listaB[j]);
      j++;
    }
  }

  for (unsigned int k = i; k < listaA.size(); k++)
    wynik.push_back(listaA[k]);

  for (unsigned int k = j; k < listaB.size(); k++)
    wynik.push_back(listaB[k]);

  return wynik;
}

void test1() {
  std::vector<int> listaA{5, 7, 11};
  std::vector<int> listaB{1, 3, 8, 14};

  std::vector<int> wynik{1, 3, 5, 7, 8, 11, 14};
  assert(polaczV1(listaA, listaB) == wynik);
}

int main() {

  test1();

  return 0;
}

