#include <iostream>

/*
Proś użytkownika o podanie liczby, dopóki nie zostanie podana liczba 7.
*/

int main() {

  int a = 0;

  while (a != 7) {
    std::cout << "Podaj liczbe: " << std::endl;
    std::cin >> a;
  }

  return 0;
}
