/*
ZAD-05 — Zamiana wartości miejscami
*/
#include <iostream>

void zamien(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  zamien(a, b);
  
  std::cout << a << std::endl;
  std::cout << b << std::endl;

  return 0;
}
