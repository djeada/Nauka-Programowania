/*
Tytul: Liczby mniejsze od podanej liczby.

Tresc: Dla otrzymanej liczby naturalnej wypisz wszystkie liczby naturalne mniejsze od niej.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczby naturalne.

Przyklad:

Dla otrzymanej liczby 3, powinny zostac wypisane liczby 2 i 1.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
for (let i = liczba - 1; i > 0; i--) {
  console.log(i);
}

