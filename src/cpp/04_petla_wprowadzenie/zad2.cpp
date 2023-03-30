/*
Tytul: Liczby mniejsze od podanej liczby.
Tresc: Dla otrzymanej liczby naturalnej wypisz wszystkie liczby naturalne
mniejsze od niej. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Liczby
naturalne. Przyklad: Dla otrzymanej liczby 3, powinny zostac wypisane liczby 2
i 1.

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int a;
  std::cin >> a;

  for (int i = 1; i < a; i++)
    std::cout << i << " ";

  std::cout << std::endl;

  return 0;
}

