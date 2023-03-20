/*
Tytuł: Obliczenie ceny podłogi.

Treść: Otrzymasz cenę pojedynczej płytki, wymiary płytki w postaci kwadratu oraz wymiary podłogi w postaci prostokąta. Oblicz, ile kosztować będzie podłoga o podanych wymiarach.

Jednostki są umowne.

Dane wejściowe: Cztery liczby naturalne: cena płytki, długość boku płytki, długość podłogi oraz szerokość podłogi.

Dane wyjściowe: Liczba naturalna oznaczająca cenę podłogi.

Przykład:

Dla pobranych liczb: 2 (cena płytki), 3 (długość boku płytki), 20 (długość podłogi) oraz 40 (szerokość podłogi), powinna zostać wypisana liczba: 196.
*/

// Pobieranie danych od użytkownika

const cena_plytki = parseInt(prompt("Podaj cenę płytki:"));
const dlugosc_boku_plytki = parseInt(prompt("Podaj długość boku płytki:"));
const dlugosc_podlogi = parseInt(prompt("Podaj długość podłogi:"));
const szerokosc_podlogi = parseInt(prompt("Podaj szerokość podłogi:"));

// Obliczanie wymiarów podłogi
const wymiary_podlogi = dlugosc_podlogi * szerokosc_podlogi;
const wymiary_plytki = dlugosc_boku_plytki ** 2;

// Obliczanie ilości płytek
const ilosc_plytek = wymiary_podlogi / wymiary_plytki;

// Obliczanie ceny podłogi
const cena_podlogi = ilosc_plytek * cena_plytki;

// Wypisanie wyniku
console.log(cena_podlogi);