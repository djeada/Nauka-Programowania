#include <iostream>

/*
Napisz funkcje, ktora dla otrzymanej liczby wypisze zaczynajac
od podstawy trojkat prostokatny rownoboczny o wysokosci rownej
otrzymanej liczbie.
*/

void trojkat(int wysokosc) {

  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x < wysokosc - y; x++)
      std::cout << "x";
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
