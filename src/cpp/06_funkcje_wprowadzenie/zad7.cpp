/*
Tytul: Haslo.
Tresc: Napisz dwie funkcje:
* Pierwsza funkcja powinna prosic uzytkownika o podanie nazwy uzytkownika i
hasla, a nastepnie zwrocic te dane.
* Druga funkcja powinna otrzymac dane od pierwszej funkcji i ponownie prosic
uzytkownika o podanie nazwy uzytkownika i hasla. Prosba o podanie danych powinna
byc umieszczona w petli. Warunkiem zakonczenia petli jest podanie przez
uzytkownika danych identycznych z tymi przekazanymi przez pierwsza funkcje. Dane
wejsciowe: dwie nazwy uzytkownika i hasla (napisy) Dane wyjsciowe: komunikat

*/
#include <iostream>
#include <string>

void inicjalizacjaDanych(std::string &nazwa, std::string &haslo) {
  std::cout << "podaj nazwe oraz haslo do zapamietania" << std::endl;
  std::cin >> nazwa >> haslo;
}

void czyDanePoprawne(std::string &nazwa, std::string &haslo) {

  std::string nowaNazwa;
  std::string noweHaslo;

  while (nowaNazwa != nazwa || noweHaslo != haslo) {
    std::cout << "Aby zalogowac sie do systemu: podaj nazwe oraz haslo"
              << std::endl;
    std::cin >> nowaNazwa >> noweHaslo;
  }

  std::cout << "Logowanie do systemu przebieglo pomyslnie" << std::endl;
}

int main() {
  std::string nazwa;
  std::string haslo;
  inicjalizacjaDanych(nazwa, haslo);
  czyDanePoprawne(nazwa, haslo);

  return 0;
}

