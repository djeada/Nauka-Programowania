/*
Tytul: Sortowanie listy binarnej.
Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer i jedynek. Posortuj te liste.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Posortowana lista liczb naturalnych.
Przyklad:
Dla listy: [1, 0, 1, 0, 1, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 1].

*/

#include <algorithm>
#include <cassert>
#include <vector>

void sortuj(std::vector<int> &lista) {
  unsigned int zera = std::count(lista.begin(), lista.end(), 0);

  for (unsigned int i = 0; i < zera; i++)
    lista[i] = 0;

  for (unsigned int i = zera; i < lista.size(); i++)
    lista[i] = 1;
}

void test1() {
  std::vector<int> lista{1, 0, 0, 1, 1, 1, 0};
  std::vector<int> wynik{0, 0, 0, 1, 1, 1, 1};

  sortuj(lista);

  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{1, 1, 1, 1, 1, 1};
  std::vector<int> wynik{1, 1, 1, 1, 1, 1};

  sortuj(lista);

  assert(lista == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

