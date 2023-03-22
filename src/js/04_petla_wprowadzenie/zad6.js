/*
Tytuł: Suma elementów ciągu.

Treść: Dla otrzymanej liczby naturalnej n, wypisz sumę n pierwszych elementów ciągu danego wzorem:

$$a_n = n^2 + n + 1$$

$$a_n = n^2 + 5n$$

$$a_n = n + 2n$$

Wynik powinien zostać zaokrąglony do najbliższej liczby naturalnej.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

* Dla otrzymanej liczby 2, w podpunkcie a) powinna zostać wypisana liczba 1.
* Dla otrzymanej liczby 2, w podpunkcie b) powinna zostać wypisana liczba 17.
* Dla otrzymanej liczby 2, w podpunkcie c) powinna zostać wypisana liczba 6.    
*/

// Pobieranie danych od użytkownika
const liczba = parseInt(prompt("Podaj liczbę:"));

// Pętla $$a_n = n^2 + n + 1$$
let suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + i + 1;
}

// Wypisanie wyniku
console.log(`a) ${suma}`);

// Pętla $$a_n = n^2 + 5n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + 5 * i;
}

// Wypisanie wyniku
console.log(`b) ${suma}`);

// Pętla $$a_n = n + 2n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i + 2 * i;
}

// Wypisanie wyniku
console.log(`c) ${suma}`);
