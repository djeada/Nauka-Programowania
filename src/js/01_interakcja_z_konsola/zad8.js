/*
Tytul: Obliczenie ceny podlogi.

Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o podanych wymiarach.

Jednostki sa umowne.

Dane wejsciowe: Cztery liczby naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc podlogi.

Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi.

Przyklad:

Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.
*/

// Pobieranie danych od uzytkownika

const cena_plytki = parseInt(prompt("Podaj cene plytki:"));
const dlugosc_boku_plytki = parseInt(prompt("Podaj dlugosc boku plytki:"));
const dlugosc_podlogi = parseInt(prompt("Podaj dlugosc podlogi:"));
const szerokosc_podlogi = parseInt(prompt("Podaj szerokosc podlogi:"));

// Obliczanie wymiarow podlogi
const wymiary_podlogi = dlugosc_podlogi * szerokosc_podlogi;
const wymiary_plytki = dlugosc_boku_plytki ** 2;

// Obliczanie ilosci plytek
const ilosc_plytek = wymiary_podlogi / wymiary_plytki;

// Obliczanie ceny podlogi
const cena_podlogi = ilosc_plytek * cena_plytki;

// Wypisanie wyniku
console.log(cena_podlogi);

