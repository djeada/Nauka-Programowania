/*
ZAD-13 — Brakujący element ciągu arytmetycznego
*/
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
  
  std::sort(lista.begin(), lista.end());
  
  int minVal = lista[0];
  int maxVal = lista[n-1];
  int sumaOczekiwana = (n + 1) * (minVal + maxVal) / 2;
  
  int sumaRzeczywista = 0;
  for (int i = 0; i < n; i++) {
    sumaRzeczywista += lista[i];
  }
  
  std::cout << (sumaOczekiwana - sumaRzeczywista) << std::endl;

  return 0;
}
