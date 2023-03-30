/*
Tytul: Rotacja w lewo/prawo.
Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.
Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

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

