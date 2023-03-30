/*
Tytul: Tabliczka mnozenia.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych wierszy i kolumn tabliczki mnozenia.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Wiersze i kolumny tabliczki mnozenia o wymiarach NxN.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
1 2 3
2 4 6
3 6 9

*/
#include <iostream>

void tabliczkaMnozenia(int n) {

  for (int y = 1; y <= n; y++) {
    for (int x = 1; x <= n; x++)
      std::cout << y * x << " ";
    std::cout << std::endl;
  }
}

int main() {

  std::cout << "Podaj liczbe: ";
  int n;
  std::cin >> n;

  tabliczkaMnozenia(n);

  return 0;
}

