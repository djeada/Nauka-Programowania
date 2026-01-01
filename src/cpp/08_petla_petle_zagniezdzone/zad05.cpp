/*
ZAD-05 — Diament z gwiazdek
*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  
  // Górna połowa diamentu
  for (int i = 0; i < (n + 1) / 2; i++) {
    for (int j = 0; j < n; j++) {
      if (j == i || j == n - 1 - i) {
        std::cout << "*";
      } else {
        std::cout << " ";
      }
    }
    std::cout << std::endl;
  }
  
  // Dolna połowa diamentu
  for (int i = (n + 1) / 2; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (j == n - 1 - i || j == i) {
        std::cout << "*";
      } else {
        std::cout << " ";
      }
    }
    std::cout << std::endl;
  }

  return 0;
}
