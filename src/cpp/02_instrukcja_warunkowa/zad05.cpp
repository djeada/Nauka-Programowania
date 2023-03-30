/*
Tytul: Posortowanie trzech liczb.
Tresc: Pobierz od uzytkownika trzy liczby naturalne i wypisz je w kolejnosci rosnacej.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Trzy liczby naturalne.
Przyklad:
Dla pobranych liczb: 2, 1 oraz 4, powinny zostac wypisane liczby: 1, 2 i 4.

*/
#include <iostream>

int main() {

  std::cout << "podaj trzy liczby:" << std::endl;

  int a;
  int b;
  int c;

  std::cin >> a;
  std::cin >> b;
  std::cin >> c;

  if (a >= b && a >= c) {
    if (b >= c)
      std::cout << c << b << a << std::endl;
    else
      std::cout << b << c << a << std::endl;
  }

  else if (c >= b && c >= a) {
    if (a >= b)
      std::cout << b << a << c << std::endl;
    else
      std::cout << a << b << c << std::endl;
  } else {
    if (a >= c)
      std::cout << c << a << b << std::endl;
    else
      std::cout << a << c << b << std::endl;
  }
  return 0;
}

