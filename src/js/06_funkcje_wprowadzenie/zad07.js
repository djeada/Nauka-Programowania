/*
ZAD-07 — Weryfikacja nazwy użytkownika i hasła

**Poziom:** ★★☆
**Tagi:** `funkcje`, `while`, `string`, `porównania`

### Treść

Napisz dwie funkcje:

1. `pobierz_dane()` — pobiera od użytkownika nazwę użytkownika i hasło i zwraca je (np. jako parę).
2. `sprawdz_dane(poprawny_login, poprawne_haslo)` — w pętli wczytuje login i hasło aż będą identyczne z przekazanymi. Po poprawnym wczytaniu wypisuje:
   `Dane poprawne. Dostęp przyznany.`

### Wejście

* `pobierz_dane()` wczytuje dwie linie:

  1. login
  2. hasło
* `sprawdz_dane(...)` wczytuje kolejne pary (login, hasło), po dwie linie na próbę.

### Wyjście

Jedna linia (tylko raz, po poprawnym dopasowaniu):

* `Dane poprawne. Dostęp przyznany.`

### Ograniczenia / gwarancje

* W pewnym momencie użytkownik poda poprawne dane.

### Uwagi o formatowaniu

* **Nie wypisuj promptów** typu „Podaj nazwę użytkownika:”.
* Porównanie jest czułe na wielkość liter.

*/

// Funkcja prosi o podanie nazwy uzytkownika i hasla, a nastepnie zwraca te dane
const pobierzDaneUzytkownika = () => {
  const nazwaUzytkownika = prompt("Podaj nazwe uzytkownika:");
  const haslo = prompt("Podaj haslo:");
  return {
    nazwaUzytkownika,
    haslo,
  };
};

// Funkcja otrzymuje dane od pierwszej funkcji i ponownie prosi o podanie nazwy uzytkownika i hasla
const sprawdzDaneUzytkownika = (poprawneDane) => {
  let daneUzytkownika;
  do {
    daneUzytkownika = pobierzDaneUzytkownika();
  } while (
    daneUzytkownika.nazwaUzytkownika !== poprawneDane.nazwaUzytkownika ||
    daneUzytkownika.haslo !== poprawneDane.haslo
  );

  console.log("Poprawne dane uzytkownika");
};

// Glowna funkcja programu
const main = () => {
  const poprawneDane = pobierzDaneUzytkownika();
  sprawdzDaneUzytkownika(poprawneDane);
};

// Uruchom program
main();

