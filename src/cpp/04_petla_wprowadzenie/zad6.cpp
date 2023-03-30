/*
Tytul: Suma elementow ciagu.
Tresc: Dla otrzymanej liczby naturalnej n, wypisz sume n pierwszych elementow
ciagu danego wzorem:
$$a_n = n^2 + n + 1$$
$$a_n = n^2 + 5n$$
$$a_n = n + 2n$$
Wynik powinien zostac zaokraglony do najblizszej liczby naturalnej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
* Dla otrzymanej liczby 2, w podpunkcie a) powinna zostac wypisana liczba 1.
* Dla otrzymanej liczby 2, w podpunkcie b) powinna zostac wypisana liczba 17.
* Dla otrzymanej liczby 2, w podpunkcie c) powinna zostac wypisana liczba 6.

*/
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(2);

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:"
      << std::endl;

  float suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = i / (i + 1);
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + "
               "5)/n wynosi:"
            << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    float a = (pow(i, 2) + 5) / i;
    suma += a;
  }
  std::cout << suma << std::endl;

  std::cout
      << "Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:"
      << std::endl;

  suma = 0;
  for (unsigned int i = 1; i <= n; i++) {
    int a = i + pow(2, i);
    suma += a;
  }

  std::cout << suma << std::endl;

  return 0;
}

