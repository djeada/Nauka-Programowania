/*
Tytuł: Ile dni ma miesiąc?

Treść: Napisz program, który dla pobranej liczby naturalnej będzie wypisywał liczbę dni w miesiącu odpowiadającemu tej liczbie. Jeśli pobrana liczba nie jest poprawnym numerem miesiąca, program powinien poinformować o tym użytkownika.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla pobranej liczby 1, program powinien zwrócić liczbę 31.
*/

// Pobieranie danych od użytkownika
const miesiac = parseInt(prompt("Podaj miesiąc:"));

// Sprawdzenie, czy liczba jest poprawna
if (miesiac > 0 && miesiac < 13) {
  // Sprawdzenie, który miesiąc odpowiada liczbie
  if (
    miesiac === 1 ||
    miesiac === 3 ||
    miesiac === 5 ||
    miesiac === 7 ||
    miesiac === 8 ||
    miesiac === 10 ||
    miesiac === 12
  ) {
    console.log("Miesiąc ma 31 dni");
  } else if (
    miesiac === 4 ||
    miesiac === 6 ||
    miesiac === 9 ||
    miesiac === 11
  ) {
    console.log("Miesiąc ma 30 dni");
  } else {
    console.log("Miesiąc ma 28 dni");
  }
} else {
  console.log("Liczba jest niepoprawna");
}
