/*
Tytul: Zamiana kolejnosci liczb.
Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze je w odwroconej kolejnosci.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Jesli uzytkownik poda liczby -7 oraz 4, program powinien wypisac liczby: 4 i -7.

*/
#include <iostream>

int main() {

  int a, b;

  std::cin >> a >> b;

  std::cout << b << std::endl << a << std::endl;

  return 0;
}

