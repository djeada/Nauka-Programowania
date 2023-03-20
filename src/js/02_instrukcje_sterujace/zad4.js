/*
Tytuł: Maksimum i minimum z dwóch liczb.

Treść: Pobierz od użytkownika dwie liczby naturalne i wypisz najpierw większą, a potem mniejszą.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla pobranych liczb: 1 oraz 4, powinny zostać wypisane liczby: 4 i 1.
*/

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));

// Porównanie ze zmienną
if (liczba_a > liczba_b) {
    console.log(liczba_a);
    console.log(liczba_b);
} else {
    console.log(liczba_b);
    console.log(liczba_a);
}