#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby wypisze 
literę Z, o wysokości równej otrzymanej liczbie.
*/

void literaZ(int wysokosc) {

  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x < wysokosc; x++) {
      if (y == 0 || y == wysokosc - 1 || x == wysokosc - y - 1)
        std::cout << "*";
      else
        std::cout << " ";
    }
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj wysokosc litery Z: ";
  int wysokosc;
  std::cin >> wysokosc;

  literaZ(wysokosc);

  return 0;
}
