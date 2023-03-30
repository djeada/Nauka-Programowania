/*
Tytul: Cyfry liczby.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry, z ktorych sie sklada,
zaczynajac od cyfry jednosci. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe:
Liczby. Przyklad: Dla otrzymanej liczby 8214, powinny zostac wypisane cyfry 4,
1, 2 i 8.

*/
#include <iostream>

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

