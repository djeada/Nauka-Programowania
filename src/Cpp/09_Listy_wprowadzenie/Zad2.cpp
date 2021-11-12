#include <iostream>
#include <vector>

/*
Dla liczby N, wczytaj N liczb do listy, a nastepnie:

a) Dodaj 1 do kazdego elementu.
b) Pomnoz kazdy element przez jego indeks.
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.

Dla kazdego podpunktu wypisz zmodyfikowana liste. Elementy listy
powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
*/

void wczytaj(std::vector<int> &lista, int n) {
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
}

void zwieksz(std::vector<int> &lista) {
  for (auto &liczba : lista)
    liczba += 1;
}

void pomnoz(std::vector<int> &lista) {
  for (unsigned int i = 0; i < lista.size(); i++)
    lista[i] *= i;
}

void zastap(std::vector<int> &lista) {
  if (lista.empty())
    return;

  for (auto &liczba : lista)
    liczba = lista[0];
}

void wypisz(std::vector<int> &lista) {
  for (auto liczba : lista)
    std::cout << liczba << ", ";
  std::cout << std::endl;
}

int main() {

  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: ";
  std::cin >> n;
  wczytaj(lista, n);

  std::vector<int> kopia(lista);
  zwieksz(kopia);
  wypisz(kopia);

  kopia = lista;
  pomnoz(kopia);
  wypisz(kopia);

  kopia = lista;
  zastap(kopia);
  wypisz(kopia);

  return 0;
}
