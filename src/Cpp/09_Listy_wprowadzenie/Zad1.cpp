#include <iostream>
#include <vector>

/*
Dla liczby N, wczytaj N liczb do listy, a następnie:

a) Wypisz listę od początku do końca. Elementy listy
powinny znajdować się w osobnych wierszach.
b) Wypisz listę od końca. Elementy listy powinny być
oddzielone przecinkami i wypisane w jednym wierszu.
*/

void wczytaj(std::vector<int> &lista, int n) {
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
}

void wypiszOdPoczatku(std::vector<int> &lista) {
  for (auto liczba : lista)
    std::cout << liczba << std::endl;
}

void wypiszOdKonca(std::vector<int> &lista) {
  auto it = cend(lista);
  while (it != cbegin(lista))
    std::cout << *(--it) << ", ";

  std::cout << std::endl;
}

int main() {

  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: " << std::endl;
  std::cin >> n;
  wczytaj(lista, n);

  std::cout << std::endl << "liczby w kolejnosci wczytania:" << std::endl;
  wypiszOdPoczatku(lista);

  std::cout << std::endl << "liczby wypisane od konca:" << std::endl;
  wypiszOdKonca(lista);

  return 0;
}
