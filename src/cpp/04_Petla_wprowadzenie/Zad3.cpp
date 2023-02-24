#include <iomanip>
#include <iostream>
#include <numbers>

/*
Dla pobranej liczby, wypisz liczbe Pi tyle razy
ile wynosi pobrana liczba, z dokladnoscia do tylu
miejsc po przecinku ile wynosi pobrana liczba.
*/

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(n);

  for (int i = 0; i < n; i++)
    std::cout << std::numbers::pi << " ";

  return 0;
}

// g++-10 -Wall -Wextra -std=c++20 Zad3.cpp -o exe
