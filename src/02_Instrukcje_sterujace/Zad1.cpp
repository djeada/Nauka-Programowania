#include <iostream>

/*
Wypisz pobraną od użytkownika liczbę, jeśli jest ona większa niż 5.
*/

int main() {

  std::cout << "podaj liczbe:" << std::endl;
  int x;
  std::cin >> x;

  if (x > 5)
    std::cout << x << std::endl;

  return 0;
}
