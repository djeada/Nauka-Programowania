/*
ZAD-03A — Mnożenie przy pomocy dodawania
ZAD-03B — Dzielenie całkowite przy pomocy odejmowania
*/
#include <iostream>

// ZAD-03A
int iloczyn(int a, int b) {
  int wynik = 0;
  for (int i = 0; i < b; i++) {
    wynik += a;
  }
  return wynik;
}

// ZAD-03B
int iloraz(int a, int b) {
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
  
  std::cout << iloczyn(a, b) << std::endl;
  std::cout << iloraz(a, b) << std::endl;

  return 0;
}
