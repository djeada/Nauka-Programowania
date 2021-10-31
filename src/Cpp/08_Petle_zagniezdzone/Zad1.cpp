#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby wypisze kwadrat 
o boku równym otrzymanej liczbie.
*/

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
