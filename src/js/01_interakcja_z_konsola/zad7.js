/*
Tytul: Pole powierzchni i objetosc figur geometrycznych.

Tresc zadania: Napisz program, ktory bedzie obliczal pola powierzchni i objetosci figur geometrycznych zgodnie z nastepujacymi instrukcjami:

a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.

b) Pobierz dlugosci bokow prostokata i wypisz jego pole.

c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.

d) Pobierz promien kuli i wypisz jej objetosc.

e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.

f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.

Jednostki sa dowolne.

Dane wejsciowe:

* Dwie liczby naturalne dla podpunktow a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.

Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.

Przyklad:

a) Dla pobranych liczb: 5 i 2, powinna zostac wypisana liczba: 5.

b) Dla pobranych liczb: 3 i 3, powinna zostac wypisana liczba: 4.

c) Dla pobranych liczb: 2 i 4, powinna zostac wypisana liczba: 1.

d) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 33.493.

e) Dla pobranych liczb: 3 i 2, powinna zostac wypisana liczba: 18.84.

f) Dla pobranych liczb: 2, 2 i 2, powinny zostac wypisana liczba: 8.
*/

// a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.
const base = parseInt(prompt("Podaj dlugosc podstawy trojkata:"));
const wysokosc_trojkata = parseInt(prompt("Podaj wysokosc trojkata:"));
console.log((base * wysokosc_trojkata) / 2);

// b) Pobierz dlugosci bokow prostokata i wypisz jego pole.
const side_a = parseInt(prompt("Podaj dlugosc boku a prostokata:"));
const side_b = parseInt(prompt("Podaj dlugosc boku b prostokata:"));
console.log(side_a * side_b);

// c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.
const diagonal_a = parseInt(prompt("Podaj dlugosc przekatnej a rombu:"));
const diagonal_b = parseInt(prompt("Podaj dlugosc przekatnej b rombu:"));
console.log((diagonal_a * diagonal_b) / 2);

// d) Pobierz promien kuli i wypisz jej objetosc.
const radius = parseInt(prompt("Podaj promien kuli:"));
console.log((4 / 3) * Math.PI * radius ** 3);

// e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.
const base_radius = parseInt(prompt("Podaj promien podstawy stozka:"));
const wysokosc_stozka = parseInt(prompt("Podaj wysokosc stozka:"));
console.log((Math.PI * base_radius ** 2 * wysokosc_stozka) / 3);

// f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.
const length = parseInt(prompt("Podaj dlugosc graniastoslupa:"));
const width = parseInt(prompt("Podaj szerokosc graniastoslupa:"));
const wysokosc_graniastoslupa = parseInt(
  prompt("Podaj wysokosc graniastoslupa:")
);
console.log(length * width * wysokosc_graniastoslupa);

