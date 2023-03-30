/*
Tytul: Dzien tygodnia odpowiadajacy danej liczbie.
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal
dzien tygodnia odpowiadajacy tej liczbie. Jesli otrzymano liczbe niedodatnia
badz dodatnia wieksza niz 7, program powinien wypisac komunikat informujacy
uzytkownika, ze liczba jest niepoprawna. Dane wejsciowe: Liczba naturalna. Dane
wyjsciowe: Komunikat o dniu tygodnia. Przyklad: Dla pobranej liczby 2, program
powinien wypisac napis "Wtorek".

*/
#include <iostream>

int main() {

  std::cout << "Podaj numer dnia tygodnia:" << std::endl;

  int dzien;
  std::cin >> dzien;

  switch (dzien) {
  case 1:
    std::cout << "Pierwszym dniem tygodnia jest poniedzialek." << std::endl;
    break;

  case 2:
    std::cout << "Drugim dniem tygodnia jest wtorek." << std::endl;
    break;

  case 3:
    std::cout << "Trzecim dniem tygodnia jest sroda." << std::endl;
    break;

  case 4:
    std::cout << "Czwartym dniem tygodnia jest czwartek." << std::endl;
    break;

  case 5:
    std::cout << "Piatym dniem tygodnia jest piatek." << std::endl;
    break;

  case 6:
    std::cout << "Szostym dniem tygodnia jest sobota." << std::endl;
    break;

  case 7:
    std::cout << "Siodmym dniem tygodnia jest niedziela." << std::endl;
    break;

  default:
    std::cout << "Podano niepoprawna liczbe." << std::endl;
  }

  return 0;
}

