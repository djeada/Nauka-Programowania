/*
Tytul: Ile dni ma miesiac?

Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal liczbe dni w miesiacu odpowiadajacemu tej liczbie. Jesli pobrana liczba nie jest poprawnym numerem miesiaca, program powinien poinformowac o tym uzytkownika.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla pobranej liczby 1, program powinien zwrocic liczbe 31.
*/

// Pobieranie danych od uzytkownika
const miesiac = parseInt(prompt("Podaj miesiac:"));

// Sprawdzenie, czy liczba jest poprawna
if (miesiac > 0 && miesiac < 13) {
  // Sprawdzenie, ktory miesiac odpowiada liczbie
  if (
    miesiac === 1 ||
    miesiac === 3 ||
    miesiac === 5 ||
    miesiac === 7 ||
    miesiac === 8 ||
    miesiac === 10 ||
    miesiac === 12
  ) {
    console.log("Miesiac ma 31 dni");
  } else if (
    miesiac === 4 ||
    miesiac === 6 ||
    miesiac === 9 ||
    miesiac === 11
  ) {
    console.log("Miesiac ma 30 dni");
  } else {
    console.log("Miesiac ma 28 dni");
  }
} else {
  console.log("Liczba jest niepoprawna");
}

