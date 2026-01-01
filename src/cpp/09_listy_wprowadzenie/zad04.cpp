/*
ZAD-04 — Min i max w liście
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
  
  int minVal = *std::min_element(lista.begin(), lista.end());
  int maxVal = *std::max_element(lista.begin(), lista.end());
  
  std::cout << maxVal << " " << minVal << std::endl;

  return 0;
}
