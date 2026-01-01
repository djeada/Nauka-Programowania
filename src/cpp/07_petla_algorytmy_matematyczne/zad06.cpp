/*
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)
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

int nww(int a, int b) {
  return (a * b) / nwd(a, b);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << nww(a, b) << std::endl;

  return 0;
}
