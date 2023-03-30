/*
Tytul: Kwadrat
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze kwadrat o
boku rownym tej liczbie. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe:
Komunikat. Przyklad: Dla otrzymanej liczby 2 powinno zostac wypisane:
**
**

*/
#include <iostream>

void kwadrat(int bok) {

  for (int y = 0; y < bok; y++) {
    for (int x = 0; x < bok; x++)
      std::cout << "x";
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj liczbe: ";
  int bok;
  std::cin >> bok;

  kwadrat(bok);

  return 0;
}

