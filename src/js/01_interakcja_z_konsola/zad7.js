/*
Tytuł: Pole powierzchni i objętość figur geometrycznych.

Treść zadania: Napisz program, który będzie obliczał pola powierzchni i objętości figur geometrycznych zgodnie z następującymi instrukcjami:

a) Pobierz długości podstawy i wysokości trójkąta i wypisz jego pole.

b) Pobierz długości boków prostokąta i wypisz jego pole.

c) Pobierz długości przekątnych rombu i wypisz jego pole.

d) Pobierz promień kuli i wypisz jej objętość.

e) Pobierz promień podstawy i wysokość stożka i wypisz jego objętość.

f) Pobierz długość, szerokość i wysokość graniastosłupa i wypisz jego objętość.

Jednostki są dowolne.

Dane wejściowe:

* Dwie liczby naturalne dla podpunktów a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.

Dane wyjściowe: Liczba naturalna dla wszystkich podpunktów.

Przykład:

a) Dla pobranych liczb: 5 i 2, powinna zostać wypisana liczba: 5.

b) Dla pobranych liczb: 3 i 3, powinna zostać wypisana liczba: 4.

c) Dla pobranych liczb: 2 i 4, powinna zostać wypisana liczba: 1.

d) Dla pobranej liczby: 2, powinna zostać wypisana liczba: 33.493.

e) Dla pobranych liczb: 3 i 2, powinna zostać wypisana liczba: 18.84.

f) Dla pobranych liczb: 2, 2 i 2, powinny zostać wypisana liczba: 8.
*/

// a) Pobierz długości podstawy i wysokości trójkąta i wypisz jego pole.
const base = parseInt(prompt("Podaj długość podstawy trójkąta:"));
const wysokosc_trojkata = parseInt(prompt("Podaj wysokość trójkąta:"));
console.log(base * wysokosc_trojkata / 2);

// b) Pobierz długości boków prostokąta i wypisz jego pole.
const side_a = parseInt(prompt("Podaj długość boku a prostokąta:"));
const side_b = parseInt(prompt("Podaj długość boku b prostokąta:"));
console.log(side_a * side_b);

// c) Pobierz długości przekątnych rombu i wypisz jego pole.
const diagonal_a = parseInt(prompt("Podaj długość przekątnej a rombu:"));
const diagonal_b = parseInt(prompt("Podaj długość przekątnej b rombu:"));
console.log(diagonal_a * diagonal_b / 2);

// d) Pobierz promień kuli i wypisz jej objętość.
const radius = parseInt(prompt("Podaj promień kuli:"));
console.log(4 / 3 * Math.PI * radius ** 3);

// e) Pobierz promień podstawy i wysokość stożka i wypisz jego objętość.
const base_radius = parseInt(prompt("Podaj promień podstawy stożka:"));
const wysokosc_stozka = parseInt(prompt("Podaj wysokość stożka:"));
console.log(Math.PI * base_radius ** 2 * wysokosc_stozka / 3);

// f) Pobierz długość, szerokość i wysokość graniastosłupa i wypisz jego objętość.
const length = parseInt(prompt("Podaj długość graniastosłupa:"));
const width = parseInt(prompt("Podaj szerokość graniastosłupa:"));
const wysokosc_graniastoslupa = parseInt(prompt("Podaj wysokość graniastosłupa:"));
console.log(length * width * wysokosc_graniastoslupa);