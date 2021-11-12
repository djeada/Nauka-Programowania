#include <iostream>

/*
Dla pobranej liczby, powinny zostac wypisane wszystkie
liczby naturalne mniejsze od podanej liczby.
*/

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int a;
  std::cin >> a;

  for (int i = 1; i < a; i++)
    std::cout << i << " ";

  std::cout << std::endl;

  return 0;
}
