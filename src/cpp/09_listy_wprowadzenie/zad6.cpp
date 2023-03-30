/*
Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.
Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje
w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc
-1. Dane wejsciowe: Lista liczb naturalnych. Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.

*/
#include <cassert>
#include <vector>

int policzSrednia(std::vector<int> &lista) {

  int suma = 0;

  for (auto liczba : lista)
    suma += liczba;

  return suma / lista.size();
}

bool czySredniaWLiscie(std::vector<int> &lista) {

  int srednia = policzSrednia(lista);

  for (auto liczba : lista) {
    if (liczba == srednia)
      return true;
  }

  return false;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  assert(!czySredniaWLiscie(lista));
}

void test2() {
  std::vector<int> lista{1, 2, 3};
  assert(czySredniaWLiscie(lista));
}

int main() {

  test1();
  test2();

  return 0;
}

