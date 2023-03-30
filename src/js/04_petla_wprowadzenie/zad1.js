/*
Tytul: Warunek konczacy petle.

Tresc: Pros uzytkownika o podanie liczby, dopoki nie zostanie podana liczba 7.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.
*/

// Pobieranie danych od uzytkownika
let liczba = parseInt(prompt("Podaj liczbe:"));

// Warunek konczacy petle
while (liczba !== 7) {
  liczba = parseInt(prompt("Podaj liczbe:"));
}

