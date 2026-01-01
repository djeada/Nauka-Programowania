/*
ZAD-08 — Sprawdzanie, czy liczba jest pierwsza
*/
#include <iostream>
#include <cmath>

bool czy_pierwsza(int n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  
  for (int i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) 
      return false;
  }
  
  return true;
}

int main() {
  int n;
  std::cin >> n;
  
  std::cout << (czy_pierwsza(n) ? "True" : "False") << std::endl;

  return 0;
}
