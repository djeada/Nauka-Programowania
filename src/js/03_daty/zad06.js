/*
Tytul: Poprawnosc daty.	

Tresc: Napisz program, ktory dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentuja one poprawna date. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.

Podpowiedz: Wszystkie liczby nie moga byc mniejsze od 1. Druga liczba nie moze byc wieksza niz 12 itd.

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Komunikat o poprawnosci lub niepoprawnosci daty.

Przyklad:

Dla pobranych liczb 2, 1 i 4, program powinien wypisac informacje o poprawnosci daty.
*/

// Pobieranie danych od uzytkownika
const dzien = parseInt(prompt("Podaj dzien:"));
const miesiac = parseInt(prompt("Podaj miesiac:"));
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy liczby sa poprawne
if (dzien > 0 && miesiac > 0 && rok > 0) {
  // Sprawdzenie, czy miesiac jest poprawny
  if (miesiac < 13) {
    // Sprawdzenie, czy rok jest przestepny
    if ((rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0) {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 30 ||
        (dzien === 30 && miesiac !== 2) ||
        (dzien === 29 && miesiac === 2)
      ) {
        console.log("Data jest poprawna");
      } else {
        console.log("Data jest niepoprawna");
      }
    } else {
      // Sprawdzenie, czy dzien jest poprawny
      if (
        dzien < 29 ||
        (dzien === 29 && miesiac !== 2) ||
        (dzien === 28 && miesiac === 2)
      ) {
        console.log("Data jest poprawna");
      } else {
        console.log("Data jest niepoprawna");
      }
    }
  } else {
    console.log("Data jest niepoprawna");
  }
} else {
  console.log("Data jest niepoprawna");
}

