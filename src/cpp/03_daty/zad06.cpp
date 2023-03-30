/*
Tytul: Poprawnosc daty.
Tresc: Napisz program, ktory dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentuja one poprawna date. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
Podpowiedz: Wszystkie liczby nie moga byc mniejsze od 1. Druga liczba nie moze byc wieksza niz 12 itd.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Komunikat o poprawnosci lub niepoprawnosci daty.
Przyklad:
Dla pobranych liczb 2, 1 i 4, program powinien wypisac informacje o poprawnosci daty.

*/
#include <iostream>

int main() {

  std::cout << "Podaj dzien, miesiac i rok: " << std::endl;

  int dzien;
  int miesiac;
  int rok;

  std::cin >> dzien;
  std::cin >> miesiac;
  std::cin >> rok;

  if (rok >= 1) {
    if (miesiac == 1 || miesiac == 3 || miesiac == 5 || miesiac == 7 ||
        miesiac == 8 || miesiac == 10 || miesiac == 12) {
      if (dzien >= 1 && dzien <= 31)
        std::cout << "Podana data jest poprawna." << std::endl;
      else
        std::cout << "Podano niepoprawna date." << std::endl;
    }

    else if (miesiac == 4 || miesiac == 6 || miesiac == 9 || miesiac == 11) {
      if (dzien >= 1 && dzien <= 30)
        std::cout << "Podana data jest poprawna." << std::endl;
      else
        std::cout << "Podano niepoprawna date." << std::endl;
    }

    else if (miesiac == 2) {
      if (rok % 4 == 0) {
        if (rok % 100 == 0) {
          if (rok % 400 == 0 && dzien >= 1 && dzien <= 29)
            std::cout << "Podana data jest poprawna." << std::endl;
          else if (dzien >= 1 && dzien <= 28)
            std::cout << "Podana data jest poprawna." << std::endl;
          else
            std::cout << "Podano niepoprawna date." << std::endl;
        } else if (dzien >= 1 && dzien <= 29)
          std::cout << "Podana data jest poprawna." << std::endl;
        else
          std::cout << "Podano niepoprawna date." << std::endl;
      } else if (dzien >= 1 && dzien <= 28)
        std::cout << "Podana data jest poprawna." << std::endl;
    }

    else
      std::cout << "Podano niepoprawna date." << std::endl;
  } else
    std::cout << "Podano niepoprawna date." << std::endl;

  return 0;
}

