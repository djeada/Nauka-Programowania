#include <iostream>

/*
Dla pobranej od uzytkownika, wypisz liczbe cyfr pobranej liczby.
*/

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int licznik = 0;

  while (liczba > 0) {
    liczba = liczba / 10;
    licznik++;
  }

  std::cout << "Podana liczba sklada sie z " << licznik << " cyfr."
            << std::endl;

  return 0;
}
