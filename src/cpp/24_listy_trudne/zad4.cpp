#include <cassert>
#include <unordered_map>
#include <vector>

/*
Otrzymujesz dwie listy binarne, A oraz B.
Znajdz dlugosc takich podciagow obu list o rownej sumie, ktorych suma jest
najwieksza. Podciagi nie musza byc takie same.
*/

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int znajdzPodciagV1(std::vector<int> &listaA, std::vector<int> &listaB) {

  if (listaA.size() != listaB.size())
    throw std::invalid_argument("Listy musza byc rownej dlugosci.");

  std::unordered_map<int, int> slownik{{0, -1}};

  int wynik = 0;
  int sumaA = 0;
  int sumaB = 0;

  for (auto i = 0; i <= listaA.size(); i++) {
    sumaA += listaA[i];
    sumaB += listaB[i];

    auto roznica = sumaA - sumaB;

    if (!slownik.count(roznica))
      slownik[roznica] = i;

    else
      wynik = std::max(wynik, i - slownik[roznica]);
  }

  return wynik;
}

// Testy Poprawnosc
void test1() {
  std::vector<int> listaA{0, 0, 1, 1, 1, 1};
  std::vector<int> listaB{0, 1, 1, 0, 1, 0};
  int wynik = 5;

  assert(znajdzPodciagV1(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{0, 0, 1, 1};
  std::vector<int> listaB{0, 1, 1, 0, 1, 0};
  try {
    znajdzPodciagV1(listaA, listaB);
    assert(false);
  } catch (...) {
    assert(true);
  }
}

int main() {

  test1();
  test2();

  return 0;
}
