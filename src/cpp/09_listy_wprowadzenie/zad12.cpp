/*
ZAD-12 — Rotacja listy w prawo o K pozycji
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
  
  int k;
  std::cin >> k;
  
  k = k % n; // Obsługa k większego niż n
  
  std::vector<int> nowa(n);
  for (int i = 0; i < n; i++) {
    nowa[(i + k) % n] = lista[i];
  }
  
  for (int i = 0; i < n; i++) {
    if (i > 0) std::cout << ",";
    std::cout << nowa[i];
  }
  std::cout << std::endl;

  return 0;
}
