/*
Tytul: Warunek trojkata.
Tresc: Dla trzech pobranych od uzytkownika dlugosci bokow sprawdz, czy mozna z
nich zbudowac trojkat. Jednostki sa umowne. Dane wejsciowe: Trzy liczby
naturalne oznaczajace dlugosci bokow trojkata. Dane wyjsciowe: Komunikat o
mozliwosci lub niemozliwosci zbudowania trojkata. Przyklad: Dla pobranych liczb:
1, 2 oraz 3, powinna zostac wypisana informacja, ze nie mozna zbudowac trojkata
z podanych bokow.

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

  if (a + b > c && b + c > a && a + c > b)
    std::cout << "z podanych bokow mozna zbudowac trojkat" << std::endl;

  else
    std::cout << "z podanych bokow nie mozna zbudowac trojkata" << std::endl;

  return 0;
}

