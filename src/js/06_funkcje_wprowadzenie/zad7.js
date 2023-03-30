/*
Tytul: Haslo.

Tresc: Napisz dwie funkcje:

* Pierwsza funkcja powinna prosic uzytkownika o podanie nazwy uzytkownika i hasla, a nastepnie zwrocic te dane.
* Druga funkcja powinna otrzymac dane od pierwszej funkcji i ponownie prosic uzytkownika o podanie nazwy uzytkownika i hasla. Prosba o podanie danych powinna byc umieszczona w petli. Warunkiem zakonczenia petli jest podanie przez uzytkownika danych identycznych z tymi przekazanymi przez pierwsza funkcje.

Dane wejsciowe: dwie nazwy uzytkownika i hasla (napisy)

Dane wyjsciowe: komunikat
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

