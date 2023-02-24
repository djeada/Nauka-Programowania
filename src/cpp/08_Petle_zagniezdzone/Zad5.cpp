#include <iostream>

/*
Napisz funkcje, ktora dla otrzymanej liczby wypisze litere X,
o wysokosci rownej otrzymanej liczbie.
*/

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
