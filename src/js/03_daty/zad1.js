/*
Tytuł: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiąca?

Treść: Wypisz pobraną od użytkownika liczbę naturalną, jeśli jest ona poprawnym numerem dnia tygodnia lub miesiąca.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

* Dla pobranej liczby: 10, powinna zostać wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna być wypisana żadna liczba.
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Porównanie ze stałą
if (liczba >= 1 && liczba <= 12) {
    console.log(liczba);
}