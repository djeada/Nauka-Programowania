/*
Tytul: Porownanie ze stala.

Tresc: Pobierz od uzytkownika liczbe naturalna. Jesli ta liczba jest wieksza niz 5, wypisz ja.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna lub brak danych wyjsciowych.

Przyklad:

Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Porownanie ze stala
if (liczba > 5) {
  console.log(liczba);
}

