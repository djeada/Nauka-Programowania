#include <cassert>
#include <vector>

/*
Dla otrzymanych dwoch list, zwroc liste, ktorej elementy są suma odpowiadajacych 
sobie elementow otrzymanych list.  Jesli listy nie sa rownej dlugosci, zaloz ze 
brakujace elementy krotszej listy sa rowne 0.
*/

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

int main() {

  test1();

  return 0;
}
