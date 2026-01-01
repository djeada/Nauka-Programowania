/*
ZAD-18 — Indeks minimum rotowanej posortowanej listy
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
  
  int indeks = 0;
  for (int i = 0; i < n - 1; i++) {
    if (lista[i] > lista[i + 1]) {
      indeks = i + 1;
      break;
    }
  }
  
  std::cout << indeks << std::endl;

  return 0;
}
