/*
Tytul: Liczba cyfr.
Tresc: Dla otrzymanej od uzytkownika liczby naturalnej wypisz liczbe cyfr, z ktorych sie sklada.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 342, powinna zostac wypisana liczba 3.

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int licznik = 0;

  while (liczba > 0) {
    liczba = liczba / 10;
    licznik++;
  }

  std::cout << "Podana liczba sklada sie z " << licznik << " cyfr."
            << std::endl;

  return 0;
}

