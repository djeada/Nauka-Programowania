/*
Tytuł: Liczby mniejsze od podanej liczby.

Treść: Dla otrzymanej liczby naturalnej wypisz wszystkie liczby naturalne mniejsze od niej.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczby naturalne.

Przykład:

Dla otrzymanej liczby 3, powinny zostać wypisane liczby 2 i 1.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla
for (let i = liczba - 1; i > 0; i--) {
    console.log(i);
}