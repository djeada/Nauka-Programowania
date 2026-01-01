/*
ZAD-01 — Wczytaj i wypisz
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
  
  // a) Wypisz od początku do końca
  for (int i = 0; i < n; i++) {
    std::cout << lista[i] << std::endl;
  }
  
  // b) Wypisz od końca do początku, oddzielone przecinkami
  for (int i = n - 1; i >= 0; i--) {
    if (i < n - 1) std::cout << ",";
    std::cout << lista[i];
  }
  std::cout << std::endl;

  return 0;
}
