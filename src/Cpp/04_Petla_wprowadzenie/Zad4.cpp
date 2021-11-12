#include <iostream>

/*
Dla pobranej liczby, powinna zostac wypisana suma
wszystkich liczb naturalnych mniejszych od pobranej liczby.
*/

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  int suma = 0;

  for (int i = 1; i < n; i++)
    suma += i;

  std::cout << suma << std::endl;

  return 0;
}
