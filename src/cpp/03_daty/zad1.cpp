/*
Tytul: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiaca?
Tresc: Wypisz pobrana od uzytkownika liczbe naturalna, jesli jest ona poprawnym
numerem dnia tygodnia lub miesiaca. Dane wejsciowe: Liczba naturalna. Dane
wyjsciowe: Liczba naturalna. Przyklad:
* Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna byc wypisana zadna liczba.

*/
#include <iostream>

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

