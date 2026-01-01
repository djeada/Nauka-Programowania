/*
ZAD-07 — Średnia dwóch największych
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
  
  std::sort(lista.begin(), lista.end(), std::greater<int>());
  
  double srednia = (lista[0] + lista[1]) / 2.0;
  
  std::cout << srednia << std::endl;

  return 0;
}
