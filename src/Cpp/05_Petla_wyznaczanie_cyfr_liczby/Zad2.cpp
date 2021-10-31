#include <iostream>

/*
Dla pobranej liczby, powinny zostac wypisane cyfry
pobranej liczby zaczynajac od cyfry jednosci.
*/

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  while (liczba > 0) {
    std::cout << liczba % 10 << std::endl;
    liczba = liczba / 10;
  }

  return 0;
}
