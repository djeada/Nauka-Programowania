/*
Tytul: Minimum oraz maksimum.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy
element tej listy i zwroc je jako dwie osobne liczby calkowite. Dane wejsciowe:
Lista liczb calkowitych. Dane wyjsciowe: Dwie liczby calkowite oznaczajace
najwiekszy i najmniejszy element z listy. Przyklad: Dla otrzymanej listy [4, -7,
8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.

*/
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
void rotacja(std::vector<int> &lista, const std::string &kierunek, int liczba) {

  if (kierunek == "prawo") {
    for (int i = 0; i < liczba; i++) {
      lista.insert(lista.begin(), lista.back());
      lista.erase(std::prev(lista.end()));
    }
  }

  else {
    for (int i = 0; i < liczba; i++) {
      lista.push_back(lista.front());
      lista.erase(lista.begin());
    }
  }
}

void test1() {

  std::vector<int> lista{5, 27, 6, 2, 1, 10, 8};
  std::vector<int> wynik{6, 2, 1, 10, 8, 5, 27};
  std::string kierunek = "lewo";
  int liczba = 2;

  rotacja(lista, kierunek, liczba);
  assert(lista == wynik);
}

void test2() {

  std::vector<int> lista{9, 9, 42, 47, 5, 6, 19, 7};
  std::vector<int> wynik{6, 19, 7, 9, 9, 42, 47, 5};
  std::string kierunek = "prawo";
  int liczba = 3;

  rotacja(lista, kierunek, liczba);
  assert(lista == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

