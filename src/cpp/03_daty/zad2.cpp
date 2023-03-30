/*
Tytul: Czy osoba jest pelnoletnia?
Tresc: Dla pobranych szesciu liczb: dnia urodzenia osoby, miesiaca urodzenia
osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiaca i
aktualnego roku, sprawdz czy dana osoba jest pelnoletnia. Dane wejsciowe: 6
liczb. Dane wyjsciowe: Komunikat. Przyklad: Dla pobranych liczb: 5, 12, 1999,
20, 11, 2020, powinna zostac wypisana informacja o pelnoletnosci osoby.

*/
#include <iostream>

int main() {

  std::cout << "Podaj trzy liczby reprezentujace dzien, miesiac i rok "
               "urodzenia osoby:"
            << std::endl;

  int dzienUrodzenia;
  int miesiacUrodzenia;
  int rokUrodzenia;

  std::cin >> dzienUrodzenia;
  std::cin >> miesiacUrodzenia;
  std::cin >> rokUrodzenia;

  std::cout << "Podaj trzy liczby reprezentujace dzisiejsza date:" << std::endl;

  int dzienAktualny;
  int miesiacAktualny;
  int rokAktualny;

  std::cin >> dzienAktualny;
  std::cin >> miesiacAktualny;
  std::cin >> rokAktualny;

  int roznicaLat = rokAktualny - rokUrodzenia;
  int roznicaMiesiecy = miesiacAktualny - miesiacUrodzenia;
  int roznicaDni = dzienAktualny - dzienUrodzenia;

  if (roznicaLat > 18)
    std::cout << "Osoba jest pelnoletnia." << std::endl;

  else if (roznicaLat == 18) {

    if (roznicaMiesiecy > 0)
      std::cout << "Osoba jest pelnoletnia." << std::endl;

    else if (roznicaMiesiecy == 0) {

      if (roznicaDni >= 0)
        std::cout << "Osoba jest pelnoletnia." << std::endl;

      else
        std::cout << "Osoba nie jest pelnoletnia." << std::endl;
    } else
      std::cout << "Osoba nie jest pelnoletnia." << std::endl;
  }

  else
    std::cout << "Osoba nie jest pelnoletnia." << std::endl;

  return 0;
}

