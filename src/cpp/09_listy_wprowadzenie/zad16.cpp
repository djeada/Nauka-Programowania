/*
ZAD-16 — Para sumująca się do zadanej wartości
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
  
  bool znaleziono = false;
  for (int i = 0; i < n && !znaleziono; i++) {
    for (int j = i + 1; j < n; j++) {
      if (lista[i] + lista[j] == suma) {
        std::cout << i << " " << j << std::endl;
        znaleziono = true;
        break;
      }
    }
  }
  
  if (!znaleziono) {
    std::cout << "-1 -1" << std::endl;
  }

  return 0;
}
