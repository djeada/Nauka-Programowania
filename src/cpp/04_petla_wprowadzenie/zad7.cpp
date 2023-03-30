/*
Tytul: Potega liczby Pi.
Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi podniesiona do potegi
rownej tej liczbie. Wynik powinien zostac zaokraglony do dwoch miejsc po
przecinku. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Liczba naturalna.
Przyklad: Dla otrzymanej liczby 1, powinna zostac wypisana liczba 3,14.

*/
#include <iomanip>
#include <iostream>

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  int wynik = 1;
  for (unsigned int i = 0; i < n; i++)
    wynik *= 3.14;

  std::cout << wynik << std::endl;

  return 0;
}

