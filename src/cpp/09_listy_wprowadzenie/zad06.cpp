/*
Tytul: Czy srednia elementow znajduje sie w liscie?
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.
Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.
Przyklad:
Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

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

