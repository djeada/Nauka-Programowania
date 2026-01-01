/*
ZAD-07 — Przybliżony pierwiastek kwadratowy (metoda Newtona)
*/
#include <iostream>
#include <cmath>

double pierwiastek(double n) {
  if (n == 0) return 0.0;
  
  double x = n;
  double epsilon = 0.00001;
  
  while (true) {
    double nx = (x + n / x) / 2.0;
    if (fabs(x - nx) < epsilon) break;
    x = nx;
  }
  
  return x;
}

int main() {
  double n;
  std::cin >> n;
  
  std::cout << pierwiastek(n) << std::endl;

  return 0;
}
