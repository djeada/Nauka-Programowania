/*
ZAD-17 — Wszystkie pary sumujące się do zadanej wartości
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
  
  int suma;
  std::cin >> suma;
  
  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (lista[i] + lista[j] == suma) {
        std::cout << lista[i] << " " << lista[j] << std::endl;
      }
    }
  }

  return 0;
}
