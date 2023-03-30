/*
Tytul: Pierwsze wystapienie klucza.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.
Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.
Przyklad:
Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.

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

