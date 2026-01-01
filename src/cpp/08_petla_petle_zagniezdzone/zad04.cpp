/*
ZAD-04 — Tabliczka mnożenia n × n
*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (j > 1) std::cout << " ";
      std::cout << (i * j);
    }
    std::cout << std::endl;
  }

  return 0;
}
