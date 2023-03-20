/*
Tytuł: Suma liczb mniejszych od podanej.

Treść: Dla otrzymanej liczby naturalnej wypisz sumę wszystkich liczb naturalnych mniejszych od niej.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba.

Przykład:

Dla otrzymanej liczby 5, powinna zostać wypisana liczba 10.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
let suma = 0;
for (let i = liczba - 1; i > 0; i--) {
    suma += i;
}

// Wypisanie wyniku
console.log(suma);