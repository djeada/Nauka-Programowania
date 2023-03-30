/*
Tytul: Cyfry liczby.

Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry, z ktorych sie sklada, zaczynajac od cyfry jednosci.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczby.

Przyklad:

Dla otrzymanej liczby 8214, powinny zostac wypisane cyfry 4, 1, 2 i 8.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  console.log(i % 10);
}

