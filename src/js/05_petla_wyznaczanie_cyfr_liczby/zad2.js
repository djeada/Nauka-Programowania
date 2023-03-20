/*
Tytuł: Cyfry liczby.

Treść: Dla otrzymanej liczby naturalnej wypisz cyfry, z których się składa, zaczynając od cyfry jedności.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczby.

Przykład:

Dla otrzymanej liczby 8214, powinny zostać wypisane cyfry 4, 1, 2 i 8.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
    console.log(i % 10);
}