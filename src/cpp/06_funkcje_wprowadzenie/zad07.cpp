/*
ZAD-07 — Weryfikacja nazwy użytkownika i hasła
*/
#include <iostream>
#include <string>

void pobierz_dane(std::string &login, std::string &haslo) {
  std::cin >> login >> haslo;
}

void sprawdz_dane(const std::string &poprawny_login, const std::string &poprawne_haslo) {
  std::string login, haslo;
  
  while (true) {
    pobierz_dane(login, haslo);
    if (login == poprawny_login && haslo == poprawne_haslo) {
      std::cout << "Dane poprawne. Dostęp przyznany." << std::endl;
      break;
    }
  }
}

int main() {
  std::string poprawny_login, poprawne_haslo;
  pobierz_dane(poprawny_login, poprawne_haslo);
  
  sprawdz_dane(poprawny_login, poprawne_haslo);

  return 0;
}
