/*
ZAD-08 — Usuń wszystkie wystąpienia klucza
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
  
  std::vector<int> nowa;
  for (int i = 0; i < n; i++) {
    if (lista[i] != klucz) {
      nowa.push_back(lista[i]);
    }
  }
  
  for (size_t i = 0; i < nowa.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << nowa[i];
  }
  std::cout << std::endl;

  return 0;
}
