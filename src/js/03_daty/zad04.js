/*
Tytul: Dzien tygodnia odpowiadajacy danej liczbie.

Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal dzien tygodnia odpowiadajacy tej liczbie. Jesli otrzymano liczbe niedodatnia badz dodatnia wieksza niz 7, program powinien wypisac komunikat informujacy uzytkownika, ze liczba jest niepoprawna.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat o dniu tygodnia.

Przyklad:

Dla pobranej liczby 2, program powinien wypisac napis "Wtorek".
*/

// Pobieranie danych od uzytkownika
const dzien_tygodnia = parseInt(prompt("Podaj dzien tygodnia:"));

// Sprawdzenie, czy liczba jest poprawna
if (dzien_tygodnia > 0 && dzien_tygodnia < 8) {
  // Sprawdzenie, ktory dzien tygodnia odpowiada liczbie
  if (dzien_tygodnia === 1) {
    console.log("Poniedzialek");
  } else if (dzien_tygodnia === 2) {
    console.log("Wtorek");
  } else if (dzien_tygodnia === 3) {
    console.log("Sroda");
  } else if (dzien_tygodnia === 4) {
    console.log("Czwartek");
  } else if (dzien_tygodnia === 5) {
    console.log("Piatek");
  } else if (dzien_tygodnia === 6) {
    console.log("Sobota");
  } else {
    console.log("Niedziela");
  }
} else {
  console.log("Liczba jest niepoprawna");
}

