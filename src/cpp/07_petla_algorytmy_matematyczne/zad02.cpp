/*
ZAD-02 — Potęgowanie a^b
*/
#include <iostream>

int potega(int a, int b) {
  int wynik = 1;
  for (int i = 0; i < b; i++) {
    wynik *= a;
  }
  return wynik;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << potega(a, b) << std::endl;

  return 0;
}
