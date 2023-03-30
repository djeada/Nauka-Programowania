/*
Tytul: Roznica miedzy dwoma listami.
Tresc: Dla otrzymanych dwoch list liczb calkowitych, znajdz elementy, ktore nie
sa czescia wspolna obu list. Dane wejsciowe: Dwie listy liczb calkowitych. Dane
wyjsciowe: Lista liczb calkowitych. Przyklad: Dla otrzymanych list [9, 2, 5, 4]
oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5, 1].

*/
#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

// Zlozonosc obliczeniowa O(n^2)
// Zlozonosc pamieciowa O(n)
std::vector<int> czescWspolnaV1(std::vector<int> &listaA,
                                std::vector<int> &listaB) {

  std::vector<int> wynik;

  for (auto liczba : listaA) {
    if (find(listaB.begin(), listaB.end(), liczba) != listaB.end())
      wynik.push_back(liczba);
  }

  return wynik;
}

// Zlozonosc obliczeniowa O(nlogn)
// Zlozonosc pamieciowa O(n)
std::vector<int> czescWspolnaV2(std::vector<int> &listaA,
                                std::vector<int> &listaB) {

  std::vector<int> wynik;
  sort(listaA.begin(), listaA.end());
  sort(listaB.begin(), listaB.end());
  set_intersection(listaA.begin(), listaA.end(), listaB.begin(), listaB.end(),
                   inserter(wynik, wynik.begin()));

  return wynik;
}

bool wektoryRowne(std::vector<int> v1, std::vector<int> v2) {
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  return v1 == v2;
}

void test1() {
  std::vector<int> listaA{3, 6, 2, 7, 9};
  std::vector<int> listaB{4, 2, 3, 5, 6};
  std::vector<int> wynik{3, 6, 2};
  assert(wektoryRowne(czescWspolnaV1(listaA, listaB), wynik));
}

void test2() {
  std::vector<int> listaA{3, 6, 2, 7, 9};
  std::vector<int> listaB{4, 2, 3, 5, 6};
  std::vector<int> wynik{3, 6, 2};
  assert(wektoryRowne(czescWspolnaV2(listaA, listaB), wynik));
}

int main() {

  test1();
  test2();

  return 0;
}

