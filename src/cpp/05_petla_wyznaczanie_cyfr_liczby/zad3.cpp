#include <iostream>

/*
Dla pobranej liczby, powinna zostac wypisana suma cyfr tej liczby.
*/

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int suma = 0;

  while (liczba > 0) {
    suma += (liczba % 10);
    liczba = liczba / 10;
  }

  std::cout << "Suma cyfr podanej liczby wynosi " << suma << std::endl;

  return 0;
}
