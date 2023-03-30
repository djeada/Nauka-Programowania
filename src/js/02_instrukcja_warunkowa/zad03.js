/*
Tytul: Znak liczby.

Tresc: Pobierz liczbe naturalna od uzytkownika i sprawdz, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla pobranej liczby: 2, powinien zostac wypisany komunikat, ze liczba jest dodatnia.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Porownanie ze stala
if (liczba > 0) {
  console.log("Liczba jest dodatnia");
} else if (liczba < 0) {
  console.log("Liczba jest ujemna");
} else {
  console.log("Liczba jest zerem");
}

