/*
ZAD-05 — Największy wspólny dzielnik (NWD)
*/
#include <iostream>

int nwd(int a, int b) {
  while (b != 0) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << nwd(a, b) << std::endl;

  return 0;
}
