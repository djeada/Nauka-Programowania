#include <iostream>

/*
Pobierz od użytkownika trzy długości boków i sprawdź, czy można z nich zbudować
trójkąt.
*/

int main() {

  std::cout << "podaj trzy liczby:" << std::endl;

  int a;
  int b;
  int c;

  std::cin >> a;
  std::cin >> b;
  std::cin >> c;

  if (a + b > c && b + c > a && a + c > b)
    std::cout << "z podanych bokow mozna zbudowac trojkat" << std::endl;

  else
    std::cout << "z podanych bokow nie mozna zbudowac trojkata" << std::endl;

  return 0;
}
