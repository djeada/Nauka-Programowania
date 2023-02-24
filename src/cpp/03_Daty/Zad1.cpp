#include <iostream>

/*
Wypisz pobrana od uzytkownika liczbe, jesli:

a) Liczba jest poprawnym numerem dnia tygodnia.
b) Liczba jest poprawnym numerem miesiaca.
*/

int main() {

  std::cout << "Podaj liczbe:" << std::endl;
  int a;
  std::cin >> a;

  if (a >= 1 && a <= 7)
    std::cout << "Liczba jest poprawnym numerem tygodnia." << std::endl;

  else
    std::cout << "Liczba nie jest poprawnym numerem tygodnia." << std::endl;

  if (a >= 1 && a <= 12)
    std::cout << "Liczba jest poprawnym numerem miesiaca." << std::endl;
  else
    std::cout << "Liczba nie jest poprawnym numerem miesiaca." << std::endl;

  return 0;
}
