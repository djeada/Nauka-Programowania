/*
Tytuł: Maks z czterech liczb.

Treść: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.

Dane wejściowe: Cztery liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla pobranych liczb: 2, 5, 1 i 4, powinna zostać wypisana liczba: 5.
*/

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));
const liczba_c = parseInt(prompt("Podaj trzecią liczbę:"));
const liczba_d = parseInt(prompt("Podaj czwartą liczbę:"));

// Znalezienie maksimum przy pomocy instrukcji warunkowej
const maks_ab = liczba_a > liczba_b ? liczba_a : liczba_b;
const maks_cd = liczba_c > liczba_d ? liczba_c : liczba_d;
const maks = maks_ab > maks_cd ? maks_ab : maks_cd;

// Wypisanie wyniku
console.log(maks);
