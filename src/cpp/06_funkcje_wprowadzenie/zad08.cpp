/*
ZAD-08 — Iloraz w dół bez / i %
*/
#include <iostream>

int zaokraglij_w_dol(int a, int b) {
  int wynik = 0;
  while (a >= b) {
    a -= b;
    wynik++;
  }
  return wynik;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << zaokraglij_w_dol(a, b) << std::endl;

  return 0;
}
