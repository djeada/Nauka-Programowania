/*
Tytuł: Porównanie ze stałą.

Treść: Pobierz od użytkownika liczbę naturalną. Jeśli ta liczba jest większa niż 5, wypisz ją.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna lub brak danych wyjściowych.

Przykład:

Dla pobranej liczby: 10, powinna zostać wypisana liczba: 10.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Porównanie ze stałą
if (liczba > 5) {
    console.log(liczba);
}