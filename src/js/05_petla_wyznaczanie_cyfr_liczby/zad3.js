/*
Tytul: Tresc: Dla otrzymanej liczby naturalnej wypisz sume cyfr tej liczby.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby 129, powinna zostac wypisana liczba 12.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let suma = 0;
for (let i = liczba; i > 0; i = Math.floor(i / 10)) {
  suma += i % 10;
}

// Wypisanie wyniku
console.log(suma);

