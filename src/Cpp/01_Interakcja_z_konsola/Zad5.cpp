#include <cmath>
#include <iostream>

/*
Wyznacz wartość funkcji w punkcie:

a) Otrzymujesz współrzędną x. Wyznacz wartość funkcji y = 3x + 10 w zadanym
punkcie. b) Pobierz współczynniki a, b oraz punkt x. Wyznacz wartość funkcji y =
ax + b w zadanym punkcie. c) Otrzymujesz współrzędną x. Wyznacz wartość funkcji
y = x3 + 22 - 20 w zadanym punkcie. d) Pobierz współczynniki a, b, c, d, m, n
oraz punkt x. Wyznacz wartość funkcji y = a*xm + b*xn + c - a w zadanym punkcie.
e) Otrzymujesz współrzędną x. Wyznacz wartość funkcji y = sin3x*cos2x + ex2 +
log(x3+2x2-x-3) w zadanym punkcie.
*/

int main() {

  std::cout << "podaj x" << std::endl;
  int x;
  std::cin >> x;

  std::cout << "3*x+10" << std::endl;
  std::cout << 3 * x + 10 << std::endl;

  std::cout << "podaj a" << std::endl;
  int a;
  std::cin >> a;

  std::cout << "podaj b" << std::endl;
  int b;
  std::cin >> b;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "a*x+b" << std::endl;
  std::cout << a * x + b << std::endl;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "y = x**3 + 2x**2 - 20" << std::endl;
  std::cout << pow(x, 3) + 2 * pow(x, 2) - 20 << std::endl;

  std::cout << "podaj a" << std::endl;
  std::cin >> a;

  std::cout << "podaj b" << std::endl;
  std::cin >> b;

  std::cout << "podaj c" << std::endl;
  int c;
  std::cin >> c;

  std::cout << "podaj d" << std::endl;
  int d;
  std::cin >> d;

  std::cout << "podaj m" << std::endl;
  int m;
  std::cin >> m;

  std::cout << "podaj n" << std::endl;
  int n;
  std::cin >> n;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "a*x**m + b*x**n + c - a" << std::endl;
  std::cout << a * pow(x, m) + b * pow(x, n) + c - a << std::endl;

  std::cout << "podaj x" << std::endl;

  std::cin >> x;

  std::cout << "sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)"
            << std::endl;
  std::cout << sin(3 * x) * cos(2 * x) + exp(pow(x, 2)) +
                   log(pow(x, 3) + 2 * pow(x, 2) - x - 3)
            << std::endl;

  return 0;
}
