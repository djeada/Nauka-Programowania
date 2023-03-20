/*
Tytuł: Treść: Dla otrzymanej liczby naturalnej wypisz sumę cyfr tej liczby.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby 129, powinna zostać wypisana liczba 12.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
let suma = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    suma += i % 10;
}

// Wypisanie wyniku
console.log(suma);