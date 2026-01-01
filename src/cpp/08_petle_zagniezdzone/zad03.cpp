/*
Tytul: Odwrocony trojkat prostokatny rownoboczny
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze,
zaczynajac od podstawy, trojkat prostokatny rownoboczny o wysokosci rownej tej
liczbie. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Komunikat. Przyklad:
Dla otrzymanej liczby 4 powinno zostac wypisane:
****
***
**
*

*/
#include <iostream>

void trojkat(int wysokosc) {
  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x < wysokosc - y; x++) std::cout << "x";
    std::cout << std::endl;
  }
}

int main() {
  std::cout << "Podaj wysokosc trojkata:" << std::endl;
  int wysokosc;
  std::cin >> wysokosc;

  trojkat(wysokosc);

  return 0;
}
