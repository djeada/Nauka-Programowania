/*
Tytul: Maksimum i minimum z dwoch liczb.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i wypisz najpierw wieksza, a potem mniejsza.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla pobranych liczb: 1 oraz 4, powinny zostac wypisane liczby: 4 i 1.

*/
#include <iostream>

int main() {

  std::cout << "podaj dwie liczby:" << std::endl;

  int a;
  int b;

  std::cin >> a;
  std::cin >> b;

  if (a > b) {
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << "pierwsza liczba jest wieksza od drugiej" << std::endl;

  }

  else {
    std::cout << b << std::endl;
    std::cout << a << std::endl;
    std::cout << "pierwsza liczba nie jest wieksza od drugiej" << std::endl;
  }

  return 0;
}

