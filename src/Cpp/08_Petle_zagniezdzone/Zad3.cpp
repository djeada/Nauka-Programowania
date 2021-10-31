#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby wypisze zaczynając 
od podstawy trójkąt prostokątny równoboczny o wysokości równej 
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
