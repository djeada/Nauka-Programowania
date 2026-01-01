/*
ZAD-04A — Minimum z dwóch liczb
ZAD-04B — Maksimum z dwóch liczb
ZAD-04C — Minimum z trzech liczb
ZAD-04D — Maksimum z trzech liczb
*/
#include <iostream>

// ZAD-04A
int min2(int a, int b) {
  return a < b ? a : b;
}

// ZAD-04B
int maks2(int a, int b) {
  return a > b ? a : b;
}

// ZAD-04C
int min3(int a, int b, int c) {
  int minAB = a < b ? a : b;
  return minAB < c ? minAB : c;
}

// ZAD-04D
int maks3(int a, int b, int c) {
  int maksAB = a > b ? a : b;
  return maksAB > c ? maksAB : c;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << min2(a, b) << std::endl;
  std::cout << maks2(a, b) << std::endl;
  
  int c;
  std::cin >> c;
  std::cout << min3(a, b, c) << std::endl;
  std::cout << maks3(a, b, c) << std::endl;

  return 0;
}
