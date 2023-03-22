/*
Tytuł: Znak liczby.

Treść: Pobierz liczbę naturalną od użytkownika i sprawdź, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranej liczby: 2, powinien zostać wypisany komunikat, że liczba jest dodatnia.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Porównanie ze stałą
if (liczba > 0) {
  console.log("Liczba jest dodatnia");
} else if (liczba < 0) {
  console.log("Liczba jest ujemna");
} else {
  console.log("Liczba jest zerem");
}
