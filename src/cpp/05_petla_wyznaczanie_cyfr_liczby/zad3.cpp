/*
Tytul: Tresc: Dla otrzymanej liczby naturalnej wypisz sume cyfr tej liczby.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 129, powinna zostac wypisana liczba 12.

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int suma = 0;

  while (liczba > 0) {
    suma += (liczba % 10);
    liczba = liczba / 10;
  }

  std::cout << "Suma cyfr podanej liczby wynosi " << suma << std::endl;

  return 0;
}

