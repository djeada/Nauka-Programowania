/*
Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Para liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).

*/
#include <algorithm>
#include <cassert>
#include <vector>

std::vector<std::pair<int, int>> znajdzParyV1(std::vector<int> &lista,
                                              int suma) {

  std::vector<std::pair<int, int>> wynik;

  for (unsigned int i = 0; i < lista.size(); i++) {
    for (unsigned int j = i + 1; j < lista.size(); j++) {
      if (lista[i] + lista[j] == suma)
        wynik.emplace_back(lista[i], lista[j]);
    }
  }

  return wynik;
}

void test1() {
  std::vector<int> lista{0, 4, 5, 6, 2, 9, 2, 3};
  std::vector<std::pair<int, int>> wynik{{0, 5}, {2, 3}, {2, 3}};
  int suma = 5;

  assert(znajdzParyV1(lista, suma) == wynik);
}

int main() {

  test1();

  return 0;
}

