/*
Tytul: Trojkat Pascala.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat
Pascala o wysokosci rownej tej liczbie. Dane wejsciowe: Liczba naturalna. Dane
wyjsciowe: Komunikat. Przyklad: Dla otrzymanej liczby 3 powinno zostac wypisane:
1
11
121

*/
#include <cmath>
#include <iostream>

void trojkatPascala(int wysokosc) {

  for (int i = 0; i < wysokosc; i++) {
    for (int j = 0; j <= i; j++) {
      std::cout << " " << (int)pow(2, i) - (int)pow(2, i - j) + (int)pow(2, j);
    }
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj wysokosc trojkata Pascala: ";
  int wysokosc;
  std::cin >> wysokosc;

  trojkatPascala(wysokosc);

  return 0;
}

