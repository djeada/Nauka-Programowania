/*
Tytul: Usun klucz.
Tresc: Dla otrzymanej listy: liczb calkowitych oraz klucza, usun pierwsze
wystapienie klucza w liscie. Dane wejsciowe: Lista liczb calkowitych i liczba
calkowita. Dane wyjsciowe: Lista liczb calkowitych. Przyklad: Dla otrzymanej
listy: [6, 2, 1, 4, 27] oraz 4, powinna zostac zwrocona lista: [6, 2, 1, 27].

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

