/*
Tytul: Wczytaj, zmodyfikuj i wypisz.
Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:
a) Dodaj 1 do kazdego elementu listy.
b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.
Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
Dane wejsciowe: N oraz N liczb calkowitych.
Dane wyjsciowe: N liczb calkowitych.
Przyklad:
Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

*/
#include <iostream>
#include <vector>

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

