#include <cmath>
#include <iostream>

/*
Wypisz wynik następujących operacji arytmetycznych dla dwóch liczb pobranych od użytkownika:

a) Suma liczb.
b) Różnica pierwszej i drugiej liczby.
c) Iloczyn liczb.
d) Iloraz pierwszej liczby przez drugą.
e) Reszta z dzielenia pierwszej liczby przez drugą.
f) Pierwsza liczba podniesiona do potęgi równej drugiej liczbie.
*/

int main() {

  int x, y;
  std::cout << "Podaj dwie liczby: " << std::endl;
  std::cin >> x >> y;

  std::cout << "Suma " << x << " oraz " << y << " wynosi " << x + y
            << std::endl;
  std::cout << "Roznica " << x << " i " << y << " wynosi " << x - y
            << std::endl;
  std::cout << "Iloczyn " << x << " i " << y << " wynosi " << x * y
            << std::endl;
  std::cout << "Iloraz " << x << " przez " << y << " wynosi " << x / y
            << std::endl;
  std::cout << "Reszta z dzielenia " << x << " przez " << y << " wynosi "
            << x % y << std::endl;
  std::cout << x << " podniesione do " << y << " wynosi " << pow(x, y)
            << std::endl;

  return 0;
}
