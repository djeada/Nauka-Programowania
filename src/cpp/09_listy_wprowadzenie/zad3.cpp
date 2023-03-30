/*
Tytul: Rotacja w lewo/prawo.
Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada
przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja
zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element
trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce.
Przesun elementy listy w podanym kierunku. Dane wejsciowe: Lista liczb
calkowitych oraz dwie liczby naturalne. Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac
zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

*/
#include <cassert>
#include <vector>

int znajdzKluczV1(std::vector<int> &lista, int klucz) {

  for (unsigned int i = 0; i < lista.size(); i++) {
    if (lista[i] == klucz)
      return i;
  }

  return -1;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  int klucz = 2;
  int wynik = 6;

  assert(znajdzKluczV1(lista, klucz) == wynik);
}

void test2() {
  std::vector<int> lista{3, -2, 4, 9, -3, -40, 8, 5, -7, -1};
  int klucz = 2;
  int wynik = -1;

  assert(znajdzKluczV1(lista, klucz) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

