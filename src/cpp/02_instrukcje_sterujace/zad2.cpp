#include <iostream>

/*
Dla dwoch pobranych od uzytkownika liczb, sprawdz czy liczby sa identyczne.
*/

int main() {

  std::cout << "podaj dwie liczby:" << std::endl;
  int a;
  int b;

  std::cin >> a;
  std::cin >> b;

  if (a == b)
    std::cout << "liczby sa jednakowe" << std::endl;
  else
    std::cout << "liczby sa rozne" << std::endl;

  return 0;
}
