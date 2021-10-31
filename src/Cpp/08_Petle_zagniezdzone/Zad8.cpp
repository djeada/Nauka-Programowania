#include <cmath>
#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby wypisze
trójkąt Pascala o wysokości równej otrzymanej liczbie.
*/

void trojkatPascala(int wysokosc) {

  for (int i = 0; i < wysokosc; i++) {
    for (int j = 0; j <= i; j++) {
      std::cout << " " << (int)pow(2, i) - (int)pow(2, i - j) + (int)pow(2, j);
    }
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj wysokosc trojkata Pascala: ";
  int wysokosc;
  std::cin >> wysokosc;

  trojkatPascala(wysokosc);

  return 0;
}
