/*
Tytul: Znak liczby.
Tresc: Pobierz liczbe naturalna od uzytkownika i sprawdz, czy liczba jest
ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat. Dane wejsciowe:
Liczba naturalna. Dane wyjsciowe: Komunikat. Przyklad: Dla pobranej liczby: 2,
powinien zostac wypisany komunikat, ze liczba jest dodatnia.

*/
#include <iostream>

int main() {

  std::cout << "podaj liczbe:" << std::endl;

  int a;
  std::cin >> a;

  if (a < 0)
    std::cout << "libczba jest ujemna" << std::endl;
  else if (a > 0)
    std::cout << "liczba jest dodatnia" << std::endl;
  else
    std::cout << "liczba jest zerem" << std::endl;

  return 0;
}

