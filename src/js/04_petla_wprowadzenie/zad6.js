/*
Tytul: Suma elementow ciagu.

Tresc: Dla otrzymanej liczby naturalnej n, wypisz sume n pierwszych elementow ciagu danego wzorem:

$$a_n = n^2 + n + 1$$

$$a_n = n^2 + 5n$$

$$a_n = n + 2n$$

Wynik powinien zostac zaokraglony do najblizszej liczby naturalnej.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

* Dla otrzymanej liczby 2, w podpunkcie a) powinna zostac wypisana liczba 1.
* Dla otrzymanej liczby 2, w podpunkcie b) powinna zostac wypisana liczba 17.
* Dla otrzymanej liczby 2, w podpunkcie c) powinna zostac wypisana liczba 6.    
*/

// Pobieranie danych od uzytkownika
const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla $$a_n = n^2 + n + 1$$
let suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + i + 1;
}

// Wypisanie wyniku
console.log(`a) ${suma}`);

// Petla $$a_n = n^2 + 5n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + 5 * i;
}

// Wypisanie wyniku
console.log(`b) ${suma}`);

// Petla $$a_n = n + 2n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i + 2 * i;
}

// Wypisanie wyniku
console.log(`c) ${suma}`);

