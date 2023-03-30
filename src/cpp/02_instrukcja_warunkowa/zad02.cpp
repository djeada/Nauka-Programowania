/*
Tytul: Porownanie ze zmienna.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i sprawdz, czy sa one identyczne. Wypisz odpowiedni komunikat.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranych liczb: 7 i 4, powinien zostac wypisany komunikat, ze liczby sa rozne.

*/
#include <iostream>

int main() {

  std::cout << "podaj dwie liczby:" << std::endl;
  int a;
  int b;

  std::cin >> a;
  std::cin >> b;

  if (a == b)
    std::cout << "liczby sa jednakowe" << std::endl;
  else
    std::cout << "liczby sa rozne" << std::endl;

  return 0;
}

