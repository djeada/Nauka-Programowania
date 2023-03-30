/*
Tytul: Konwersja listy na napis
Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

std::string liczby(const std::vector<int> &lista) {
  std::string wynik = "";

  for (auto liczba : lista)
    wynik += std::to_string(liczba);

  return wynik;
}

void test1() {
  std::vector<int> lista({2, 4, 7});
  std::string wynik = "247";
  assert(liczby(lista) == wynik);
}

void test2() {
  std::vector<int> lista;
  std::string wynik = "";
  assert(liczby(lista) == wynik);
}

int main() {
  test1();
  test2();
  return 0;
}

