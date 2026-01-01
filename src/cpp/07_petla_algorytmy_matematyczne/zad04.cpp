/*
ZAD-04 — Silnia n!
*/
#include <iostream>

int silnia(int n) {
  int wynik = 1;
  for (int i = 1; i <= n; i++) {
    wynik *= i;
  }
  return wynik;
}

int main() {
  int n;
  std::cin >> n;
  
  std::cout << silnia(n) << std::endl;

  return 0;
}
