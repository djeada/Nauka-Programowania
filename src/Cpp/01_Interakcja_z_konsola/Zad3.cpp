#include <iostream>

/*
Wypisz ciągi znaków na standardowe wyjście. Pamiętaj o spacjach i przejściach do nowej linii.

Kwadrat.
xx
xx

Trójkąt.
1
22
333

Romb z jedynek.
  1
 111
11111
 111
  1
*/

int main() {

  std::cout << "xx" << std::endl;
  std::cout << "xx" << std::endl << std::endl;

  std::cout << "1" << std::endl;
  std::cout << "22" << std::endl;
  std::cout << "333" << std::endl << std::endl;

  std::cout << "  1" << std::endl;
  std::cout << " 111" << std::endl;
  std::cout << "11111" << std::endl;
  std::cout << " 111" << std::endl;
  std::cout << "  1" << std::endl;

  return 0;
}
