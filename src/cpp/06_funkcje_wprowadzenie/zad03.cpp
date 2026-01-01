/*
ZAD-03 — Sprawdzanie warunków logicznych
*/
#include <iostream>
#include <cmath>

bool pierwszaWieksza(int a, int b) {
  return a > b;
}

bool sumaMniejsza10(int a, int b) {
  return a + b < 10;
}

bool obieNieparzyste(int a, int b) {
  return a % 2 == 1 && b % 2 == 1;
}

int wieksza(int a, int b) {
  return a > b ? a : b;
}

bool wiekszaMniejszaPierwszaKwadrat(int a, int b) {
  return wieksza(a, b) < a * a;
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  std::cout << (pierwszaWieksza(a, b) ? "True" : "False") << std::endl;
  std::cout << (sumaMniejsza10(a, b) ? "True" : "False") << std::endl;
  std::cout << (obieNieparzyste(a, b) ? "True" : "False") << std::endl;
  std::cout << (wiekszaMniejszaPierwszaKwadrat(a, b) ? "True" : "False") << std::endl;

  return 0;
}
