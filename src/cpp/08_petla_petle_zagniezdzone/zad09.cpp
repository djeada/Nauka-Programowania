/*
ZAD-09 — Pierwsze n liczb pierwszych
*/
#include <iostream>
#include <cmath>

bool czy_pierwsza(int num) {
  if (num <= 1) return false;
  if (num <= 3) return true;
  if (num % 2 == 0 || num % 3 == 0) return false;
  
  for (int i = 5; i * i <= num; i += 6) {
    if (num % i == 0 || num % (i + 2) == 0) 
      return false;
  }
  
  return true;
}

int main() {
  int n;
  std::cin >> n;
  
  int count = 0;
  int num = 2;
  
  while (count < n) {
    if (czy_pierwsza(num)) {
      if (count > 0) std::cout << " ";
      std::cout << num;
      count++;
    }
    num++;
  }
  std::cout << std::endl;

  return 0;
}
