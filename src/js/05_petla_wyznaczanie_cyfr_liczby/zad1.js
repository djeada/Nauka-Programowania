/*
Tytuł: Liczba cyfr.

Treść: Dla otrzymanej od użytkownika liczby naturalnej wypisz liczbę cyfr, z których się składa.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby 342, powinna zostać wypisana liczba 3.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
let cyfry = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    cyfry++;
}

// Wypisanie wyniku
console.log(cyfry);