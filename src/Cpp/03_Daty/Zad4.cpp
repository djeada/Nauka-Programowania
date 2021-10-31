#include <iostream>

/*
Dla pobranej liczby, wypisz dzień tygodnia odpowiadający tej liczbie.
Jeśli otrzymano liczbę niedodatnią, bądź dodatnią większą niż 7,
wypisz komuniat informujący użytkownika, że liczba jest niepoprawna.
*/

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
