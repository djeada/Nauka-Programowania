/*
ZAD-03 — Pierwsze wystąpienie klucza
*/
#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
  
  int klucz;
  std::cin >> klucz;
  
  int wynik = -1;
  for (size_t i = 0; i < lista.size(); i++) {
    if (lista[i] == klucz) {
      wynik = i;
      break;
    }
  }
  
  std::cout << wynik << std::endl;

  return 0;
}
