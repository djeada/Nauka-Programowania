/*
Tytul: Litera X.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere X o
wysokosci rownej tej liczbie. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe:
Komunikat. Przyklad: Dla otrzymanej liczby 4 powinno zostac wypisane:
*   *
* *
* *
*   *

*/
#include <iostream>

void literaX(int wysokosc) {
  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x < wysokosc; x++) {
      if (y == x || x == (wysokosc - 1 - y))
        std::cout << "*";
      else
        std::cout << " ";
    }
    std::cout << std::endl;
  }
}

int main() {
  std::cout << "Podaj wysokosc: ";
  int wysokosc;
  std::cin >> wysokosc;

  literaX(wysokosc);

  return 0;
}
