#include <cmath>
#include <iomanip>
#include <iostream>

/*
Dla pobranej liczby n, wypisz sume n pierwszych wyrazow ciagu danego wzorem:

a) a_n = n/(n + 1)
b) a_n = (n^2 + 5)/n
c) a_n = n + 2^n

Wynik powinien byc zaokraglony do najblizszej liczby naturalnej.
*/

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:"
      << std::endl;

  float suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = i / (i + 1);
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + "
               "5)/n wynosi:"
            << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = (pow(i, 2) + 5) / i;
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:"
      << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    int a = i + pow(2, i);
    suma += a;
  }

  std::cout << suma << std::endl;

  return 0;
}
