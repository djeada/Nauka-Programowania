/*
ZAD-10 — Czy punkty są współliniowe
*/
#include <iostream>
#include <cmath>

int main() {
  int xA, yA, xB, yB, xC, yC;
  std::cin >> xA >> yA >> xB >> yB >> xC >> yC;
  
  // Oblicz pole trójkąta
  double pole = abs((xB - xA) * (yC - yA) - (xC - xA) * (yB - yA)) / 2.0;
  
  std::cout << (pole == 0 ? "Tak" : "Nie") << std::endl;

  return 0;
}
