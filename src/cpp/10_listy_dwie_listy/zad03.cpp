/*
Tytul: Suma elementow dwoch list.
Tresc: Dla otrzymanych dwoch list, zwroc liste, ktorej elementy sa suma odpowiadajacych sobie elementow obu list. Jesli listy nie sa tej samej dlugosci, zaloz, ze brakujace elementy krotszej listy sa rowne 0.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanych list [3, 1, 2, 5] oraz [2, 8, 6, 5], zostanie zwrocona lista: [5, 9, 8, 10].

*/
#include <cassert>
#include <vector>

std::vector<int> suma(std::vector<int> &listaA, std::vector<int> &listaB) {

  std::vector<int> wynik(listaA);

  unsigned int n = wynik.size() < listaB.size() ? wynik.size() : listaB.size();

  for (unsigned int i = 0; i < n; i++)
    wynik[i] += listaB[i];

  for (unsigned int i = n; i < listaB.size(); i++)
    wynik.push_back(listaB[i]);

  return wynik;
}

void test1() {
  std::vector<int> listaA{3, 1, 2, 5};
  std::vector<int> listaB{2, 8, 6, 5};

  std::vector<int> wynik{5, 9, 8, 10};
  assert(suma(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{3, 1, 2, 5};
  std::vector<int> listaB{2, 8};

  std::vector<int> wynik{5, 9, 2, 5};
  assert(suma(listaA, listaB) == wynik);
}

void test3() {
  std::vector<int> listaA{3, 1};
  std::vector<int> listaB{2, 8, 6, 5};

  std::vector<int> wynik{5, 9, 6, 4};
  assert(suma(listaA, listaB) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

