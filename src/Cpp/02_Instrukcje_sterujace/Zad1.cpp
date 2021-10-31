#include <iostream>

/*
Wypisz pobrana od uzytkownika liczbe, jesli jest ona wieksza niz 5.
*/

int main() {

  std::cout << "podaj liczbe:" << std::endl;
  int x;
  std::cin >> x;

  if (x > 5)
    std::cout << x << std::endl;

  return 0;
}
