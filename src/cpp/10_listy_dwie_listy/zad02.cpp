/*
Tytul: Polaczenie dwoch list.
Tresc: Dla otrzymanych dwoch list, zwroc liste, ktora powstala poprzez:
a) Dostawienie drugiej listy na koniec pierwszej listy.
b) Wstawienie elementow o indeksach parzystych z drugiej listy na odpowiadajace im indeksy pierwszej listy.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanych list [1, 2, 3] oraz [4, 5, 6], w podpunkcie a) powinna zostac zwrocona lista: [1, 2, 3, 4, 5, 6].
W podpunkcie b) powinna zostac zwrocona lista: [4, 2, 6, 3].

*/
#include <cassert>
#include <vector>

std::vector<int> dostaw(std::vector<int> &listaA, std::vector<int> &listaB) {

  std::vector<int> wynik(listaA);

  for (auto liczba : listaB)
    wynik.push_back(liczba);

  return wynik;
}

std::vector<int> podmien(std::vector<int> &listaA, std::vector<int> &listaB) {
  std::vector<int> wynik(listaA);

  for (unsigned int i = 0; i < wynik.size(); i += 2)
    wynik[i] = listaB[i];

  return wynik;
}

void test1() {
  std::vector<int> listaA{-2, 8, 3, 6};
  std::vector<int> listaB{7, 5, 0};

  std::vector<int> wynik{-2, 8, 3, 6, 7, 5, 0};
  assert(dostaw(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{-2, 8, 3, 6};
  std::vector<int> listaB{7, 5, 0};

  std::vector<int> wynik{7, 8, 0, 6};
  assert(podmien(listaA, listaB) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

