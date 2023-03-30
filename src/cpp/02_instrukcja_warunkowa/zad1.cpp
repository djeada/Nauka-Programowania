/*
Tytul: Porownanie ze stala.
Tresc: Pobierz od uzytkownika liczbe naturalna. Jesli ta liczba jest wieksza niz
5, wypisz ja. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: Liczba naturalna
lub brak danych wyjsciowych. Przyklad: Dla pobranej liczby: 10, powinna zostac
wypisana liczba: 10.

*/
#include <iostream>

int main() {

  std::cout << "podaj liczbe:" << std::endl;
  int x;
  std::cin >> x;

  if (x > 5)
    std::cout << x << std::endl;

  return 0;
}

