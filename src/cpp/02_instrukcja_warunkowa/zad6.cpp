/*
Tytul: Maks z czterech liczb.
Tresc: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.
Dane wejsciowe: Cztery liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla pobranych liczb: 2, 5, 1 i 4, powinna zostac wypisana liczba: 5.

*/
#include <iostream>

int main() {

  std::cout << "podaj cztery liczby:" << std::endl;

  int a;
  int b;
  int c;
  int d;

  std::cin >> a;
  std::cin >> b;
  std::cin >> c;
  std::cin >> d;

  int maksAB = a > b ? a : b;
  int maksCD = c > d ? c : d;
  int maks = maksAB > maksCD ? maksAB : maksCD;

  std::cout << maks << std::endl;

  return 0;
}

