/*
Tytul: Liczba cyfr.

Tresc: Dla otrzymanej od uzytkownika liczby naturalnej wypisz liczbe cyfr, z ktorych sie sklada.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby 342, powinna zostac wypisana liczba 3.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let cyfry = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  cyfry++;
}

// Wypisanie wyniku
console.log(cyfry);

