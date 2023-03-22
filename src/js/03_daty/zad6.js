/*
Tytuł: Poprawność daty.	

Treść: Napisz program, który dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentują one poprawną datę. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem.

Podpowiedź: Wszystkie liczby nie mogą być mniejsze od 1. Druga liczba nie może być większa niż 12 itd.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Komunikat o poprawności lub niepoprawności daty.

Przykład:

Dla pobranych liczb 2, 1 i 4, program powinien wypisać informację o poprawności daty.
*/

// Pobieranie danych od użytkownika
const dzien = parseInt(prompt("Podaj dzień:"));
const miesiac = parseInt(prompt("Podaj miesiąc:"));
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy liczby są poprawne
if (dzien > 0 && miesiac > 0 && rok > 0) {
  // Sprawdzenie, czy miesiąc jest poprawny
  if (miesiac < 13) {
    // Sprawdzenie, czy rok jest przestępny
    if ((rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0) {
      // Sprawdzenie, czy dzień jest poprawny
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
      // Sprawdzenie, czy dzień jest poprawny
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
