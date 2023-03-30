/*
Tytul: Wypisanie elementow macierzy spiralnie.
Tresc: Otrzymujesz liste list liczb naturalnych. Zbierz elementy otrzymanej
macierzy spiralnie i zapisz je w liscie. Dane wejsciowe: Lista list liczb
naturalnych. Dane wyjsciowe: Lista. Przyklad: Dla otrzymanej macierzy: [[1,2,3],
[4,5,6], [7,8,9]], powinna zostac zwrocona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].

*/
#include <algorithm>
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::pair<int, int>>
polaczPrzedzialyV1(std::vector<std::pair<int, int>> &lista) {
  /**
   *
   */
  sort(lista.begin(), lista.end());

  int pocz = lista.front().first;
  int koniec = lista.front().second;
  lista.erase(lista.begin());

  std::vector<std::pair<int, int>> wynik;

  for (const auto &para : lista) {
    if (koniec >= para.first) {
      if (koniec < para.second)
        koniec = para.second;
    } else {
      wynik.push_back(std::pair<int, int>(pocz, koniec));
      pocz = para.first;
      koniec = para.second;
    }
  }

  wynik.push_back(std::pair<int, int>(pocz, koniec));

  return wynik;
}

void test1() {
  std::vector<std::pair<int, int>> lista{{23, 67}, {23, 53}, {45, 88}, {77, 88},
                                         {10, 22}, {11, 12}, {42, 45}};

  std::vector<std::pair<int, int>> wynik{{10, 22}, {23, 88}};
  assert(polaczPrzedzialyV1(lista) == wynik);
}

int main() {
  test1();
  return 0;
}

