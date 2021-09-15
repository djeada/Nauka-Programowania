#include <iostream>
#include <vector>

// Dla liczby N, wczytaj N liczb do listy, a nastepnie:
// a) wypisz liste od poczatku do konca. Elementy listy powinny
// znajdowac sie w osobnych wierszach.
// b) wypisz liste od konca. Elementy listy powinny byc oddzielone
// przecinkami i wypisane w jednym wierszu.

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
  
  std::cout << std::endl <<"liczby wypisane od konca:" << std::endl;
  wypiszOdKonca(lista);

  return 0;
}
