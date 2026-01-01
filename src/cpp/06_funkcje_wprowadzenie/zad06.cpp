/*
ZAD-06 — Suma cyfr liczby (funkcja)
*/
#include <iostream>

int sumaCyfr(int liczba) {
  int suma = 0;
  while (liczba > 0) {
    suma += (liczba % 10);
    liczba /= 10;
  }
  return suma;
}

int main() {
  int n;
  std::cin >> n;
  
  std::cout << sumaCyfr(n) << std::endl;

  return 0;
}
