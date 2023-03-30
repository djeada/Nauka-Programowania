/*
Tytul: Mnozenie wektorowe.
Tresc: Tresc: Otrzymujesz dwie listy liczb calkowitych reprezentujace dwa
wektory trojwymiarowej przestrzeni euklidesowej. Zaimplementuj mnozenie
wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni
euklidesowej). Dane wejsciowe: Dwie listy liczb calkowitych o dlugosci 3. Dane
wyjsciowe: Liczba naturalna. Przyklad: Dla otrzymanych list [1, 2, 3] oraz [3,
1, 2], powinno zostac zwrocone: 5.

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

