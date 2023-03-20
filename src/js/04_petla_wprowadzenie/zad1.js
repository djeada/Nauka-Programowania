/*
Tytuł: Warunek kończący pętle.

Treść: Proś użytkownika o podanie liczby, dopóki nie zostanie podana liczba 7.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.
*/

// Pobieranie danych od użytkownika
let liczba = parseInt(prompt("Podaj liczbę:"));

// Warunek kończący pętle
while (liczba !== 7) {
    liczba = parseInt(prompt("Podaj liczbę:"));
}