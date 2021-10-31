#include <iostream>

/*
Napisz funkcję, która dla otrzymanej liczby N,
wypisze N pierwszych wierszy i kolumn tabliczki
mnożenia.
*/

void tabliczkaMnozenia(int n) {

  for (int y = 1; y <= n; y++) {
    for (int x = 1; x <= n; x++)
      std::cout << y * x << " ";
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj liczbe: ";
  int n;
  std::cin >> n;

  tabliczkaMnozenia(n);

  return 0;
}
