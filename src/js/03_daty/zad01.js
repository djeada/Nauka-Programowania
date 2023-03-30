/*
Tytul: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiaca?

Tresc: Wypisz pobrana od uzytkownika liczbe naturalna, jesli jest ona poprawnym numerem dnia tygodnia lub miesiaca.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

* Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna byc wypisana zadna liczba.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Porownanie ze stala
if (liczba >= 1 && liczba <= 12) {
  console.log(liczba);
}

