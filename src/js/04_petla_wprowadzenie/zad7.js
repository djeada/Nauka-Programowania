/*
Tytul: Potega liczby Pi.

Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi podniesiona do potegi rownej tej liczbie. Wynik powinien zostac zaokraglony do dwoch miejsc po przecinku.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad: Dla otrzymanej liczby 1, powinna zostac wypisana liczba 3,14.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let wynik = Math.PI;
for (let i = 1; i < liczba; i++) {
  wynik *= Math.PI;
}

// Wypisanie wyniku
console.log(wynik.toFixed(2));

