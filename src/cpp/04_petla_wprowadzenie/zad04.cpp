/*
Tytul: Suma liczb mniejszych od podanej.
Tresc: Dla otrzymanej liczby naturalnej wypisz sume wszystkich liczb naturalnych mniejszych od niej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba.
Przyklad:
Dla otrzymanej liczby 5, powinna zostac wypisana liczba 10.

*/
#include <iostream>

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  int suma = 0;

  for (int i = 1; i < n; i++)
    suma += i;

  std::cout << suma << std::endl;

  return 0;
}

