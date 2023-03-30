/*
Tytul: Maks z czterech liczb.

Tresc: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.

Dane wejsciowe: Cztery liczby naturalne.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla pobranych liczb: 2, 5, 1 i 4, powinna zostac wypisana liczba: 5.
*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));
const liczba_c = parseInt(prompt("Podaj trzecia liczbe:"));
const liczba_d = parseInt(prompt("Podaj czwarta liczbe:"));

// Znalezienie maksimum przy pomocy instrukcji warunkowej
const maks_ab = liczba_a > liczba_b ? liczba_a : liczba_b;
const maks_cd = liczba_c > liczba_d ? liczba_c : liczba_d;
const maks = maks_ab > maks_cd ? maks_ab : maks_cd;

// Wypisanie wyniku
console.log(maks);

