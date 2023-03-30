/*
Tytul: Choinka.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N trojkatow ustawionych w kolumnie, jeden na drugim. Wysokosc pierwszego trojkata to 1, a kazdego nastepnego jest rowna wysokosci poprzedniego powiekszonej o 1.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
*
*
**
*
**
***

*/
#include <iostream>

void trojkat(int wysokosc) {

  for (int y = 0; y < wysokosc; y++) {
    for (int x = 0; x <= y; x++)
      std::cout << "*";
    std::cout << std::endl;
  }
}

void choinka(int wysokosc) {

  for (int i = 1; i <= wysokosc; i++)
    trojkat(i);
}

int main() {

  std::cout << "Podaj wysokosc choinki: ";
  int wysokosc;
  std::cin >> wysokosc;

  choinka(wysokosc);

  return 0;
}

