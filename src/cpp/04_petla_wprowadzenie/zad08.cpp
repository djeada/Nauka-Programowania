/*
Tytul: Liczba kur i owiec na farmie.
Tresc: Na farmie jest a glow i b nog. Znajdz liczbe kur i liczbe owiec.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla otrzymanych liczb 40 i 100, powinny zostac wypisane liczby 30 i 10.

*/
#include <iostream>

int main() {

  std::cout << "Podaj dwie liczby: " << std::endl;
  int glowy, nogi;
  std::cin >> glowy >> nogi;

  for (int i = 0; i < glowy; i++) {
    int owce = glowy - i;
    if (2 * i + 4 * owce == nogi) {
      std::cout << i << " " << owce << std::endl;
      break;
    }
  }

  return 0;
}

