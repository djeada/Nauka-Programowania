/*
Tytul: Liczba pi.
Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi tyle razy, ile wynosi ta liczba, z dokladnoscia do tylu miejsc po przecinku, ile wynosi otrzymana liczba.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 2, powinno zostac wypisane:
3,14
3,14

*/
#include <iomanip>
#include <iostream>
#include <numbers>

int main() {

  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(n);

  for (int i = 0; i < n; i++)
    std::cout << std::numbers::pi << " ";

  return 0;
}

// g++-10 -Wall -Wextra -std=c++20 Zad3.cpp -o exe

