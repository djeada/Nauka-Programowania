/*
Tytul: Suma liczb mniejszych od podanej.

Tresc: Dla otrzymanej liczby naturalnej wypisz sume wszystkich liczb naturalnych mniejszych od niej.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba.

Przyklad:

Dla otrzymanej liczby 5, powinna zostac wypisana liczba 10.
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla
let suma = 0;
for (let i = liczba - 1; i > 0; i--) {
  suma += i;
}

// Wypisanie wyniku
console.log(suma);

