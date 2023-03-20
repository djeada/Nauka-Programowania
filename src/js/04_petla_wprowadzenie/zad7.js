/*
Tytuł: Potęga liczby Pi.

Treść: Dla otrzymanej liczby naturalnej wypisz liczbę Pi podniesioną do potęgi równej tej liczbie. Wynik powinien zostać zaokrąglony do dwóch miejsc po przecinku.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład: Dla otrzymanej liczby 1, powinna zostać wypisana liczba 3,14.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
let wynik = Math.PI;
for (let i = 1; i < liczba; i++) {
    wynik *= Math.PI;
}

// Wypisanie wyniku
console.log(wynik.toFixed(2));