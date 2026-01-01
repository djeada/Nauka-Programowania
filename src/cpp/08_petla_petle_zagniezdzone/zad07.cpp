/*
ZAD-07 — Wszystkie trójkąty do wysokości n
*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  
  for (int h = 1; h <= n; h++) {
    for (int i = 1; i <= h; i++) {
      for (int j = 0; j < i; j++) {
        std::cout << "*";
      }
      std::cout << std::endl;
    }
  }

  return 0;
}
