/*
Tytul: Trojkat prostokatny rownoboczny
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat
prostokatny rownoboczny o wysokosci rownej tej liczbie. Dane wejsciowe: Liczba
naturalna. Dane wyjsciowe: Komunikat. Przyklad: Dla otrzymanej liczby 3 powinno
zostac wypisane:
*
**
***

*/
#include <iostream>

void trojkat(int wysokosc) {
  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x <= y; x++) std::cout << "x";
    std::cout << std::endl;
  }
}

int main() {
  std::cout << "Podaj wysokosc trojkata: ";
  int wysokosc;
  std::cin >> wysokosc;

  trojkat(wysokosc);

  return 0;
}
