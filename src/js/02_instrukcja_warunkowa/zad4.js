/*
Tytul: Maksimum i minimum z dwoch liczb.

Tresc: Pobierz od uzytkownika dwie liczby naturalne i wypisz najpierw wieksza, a potem mniejsza.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Dla pobranych liczb: 1 oraz 4, powinny zostac wypisane liczby: 4 i 1.
*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
if (liczba_a > liczba_b) {
  console.log(liczba_a);
  console.log(liczba_b);
} else {
  console.log(liczba_b);
  console.log(liczba_a);
}

