/*
Tytul: Usun duplikaty.
Tresc: Otrzymujesz liste liczb naturalnych. Usun z niej wszystkie duplikaty, tak
aby kazda liczba pozostala tylko raz. Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostac zwrocona lista: [3, 2,
1].

*/
#include <algorithm>
#include <cassert>
#include <vector>

std::pair<int, int> sumaDwochV1(std::vector<int> &lista, int liczba) {
  int n = lista.size();

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (lista[j] + lista[i] == liczba)
        return std::pair<int, int>(i, j);
    }
  }

  return std::pair<int, int>(-1, -1);
}

void test1() {
  std::vector<int> lista{1, 3, 4, 5, 2};
  int liczba = 5;
  std::pair<int, int> wynik(0, 2);
  assert(sumaDwochV1(lista, liczba) == wynik);
}

void test2() {
  std::vector<int> lista{2, -6, 10, 21, 8};
  int liczba = 7;
  std::pair<int, int> wynik(-1, -1);
  assert(sumaDwochV1(lista, liczba) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

