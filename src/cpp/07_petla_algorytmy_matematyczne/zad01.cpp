/*
ZAD-01 — Obliczanie średniej z n liczb
*/
#include <iostream>

float srednia(int n) {
  float suma = 0.0;
  float x;
  
  for (int i = 0; i < n; i++) {
    std::cin >> x;
    suma += x;
  }
  
  return suma / n;
}

int main() {
  int n;
  std::cin >> n;
  
  float wynik = srednia(n);
  std::cout << wynik << std::endl;

  return 0;
}
