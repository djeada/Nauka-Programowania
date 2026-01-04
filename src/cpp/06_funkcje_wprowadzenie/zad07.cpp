/*
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca
je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i
hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje: `Dane
poprawne. Dostęp przyznany.`

### Wejście

* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na
próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
* Porównanie jest czułe na wielkość liter.

*/
#include <iostream>
#include <string>

void pobierz_dane(std::string &login, std::string &haslo) {
  std::cin >> login >> haslo;
}

void sprawdz_dane(const std::string &poprawny_login,
                  const std::string &poprawne_haslo) {
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
