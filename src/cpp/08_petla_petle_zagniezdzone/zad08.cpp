/*
ZAD-08 — Trójkąt Pascala
*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  
  for (int i = 0; i < n; i++) {
    int c = 1;
    for (int j = 0; j <= i; j++) {
      if (j > 0) std::cout << " ";
      std::cout << c;
      c = c * (i - j) / (j + 1);
    }
    std::cout << std::endl;
  }

  return 0;
}
