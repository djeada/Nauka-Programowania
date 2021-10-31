#include <iostream>
#include <string>

/*
Napisz dwie funkcje. Pierwsza powinna prosić użytkownika o podanie nazwy oraz
hasła oraz zwracać otrzymane dane. Druga powinna otrzymywać dane od pierwszej i
ponownie prosić o podanie nazwy oraz hasła. Prośba o podanie danych powinna
zostać umieszczona w pętli. Warunkiem zakończenia pętli jest podanie przez
użytkownika danych identycznych z tymi przekazanymi przez pierwszą funkcję.
*/

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
