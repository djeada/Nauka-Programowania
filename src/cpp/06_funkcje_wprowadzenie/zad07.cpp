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
