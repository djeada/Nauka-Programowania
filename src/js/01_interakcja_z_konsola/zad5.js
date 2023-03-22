/*
Tytuł: Obliczanie wartości funkcji w danym punkcie.

Treść zadania: Napisz program, który będzie obliczać wartość funkcji w danym punkcie zgodnie z następującymi instrukcjami:

a) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = 3x + 10$ w tym punkcie.

b) Pobierz współczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax + b$ w tym punkcie.

c) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = x^3 + 22 - 20$ w tym punkcie.

d) Pobierz współczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.

e) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.

Dane wejściowe:

* Liczba naturalna dla punktów 1, 3 i 5.
* Trzy liczby naturalne dla punktu 2.
* Sześć liczb naturalnych dla punktu 4.

Dane wyjściowe:

* Liczba naturalna dla punktów 1, 2, 3 i 4.
* Liczba zmiennoprzecinkowa dla punktu 5.

Przykład:

a) Jeśli otrzymasz współrzędną $x = 3$, program powinien wypisać liczbę 19.

b) Jeśli pobierzesz liczby 1, 2 i 3, program powinien wypisać liczbę 5.

c) Jeśli otrzymasz współrzędną $x = 5$, program powinien wypisać liczbę 155.

d) Jeśli pobierzesz liczby 1, 1, 1, 1, 1 i 1, program powinien wypisać liczbę 2.
 
e) Jeśli otrzymasz współrzędną $x = 2$, program powinien wypisać liczbę 57.179.
*/
// a) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = 3x + 10$ w tym punkcie.
const x1 = parseInt(prompt("Podaj współrzędną x:"));
console.log(3 * x1 + 10);

// b) Pobierz współczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax + b$ w tym punkcie.
const a2 = parseInt(prompt("Podaj współczynnik a:"));
const b2 = parseInt(prompt("Podaj współczynnik b:"));
const x2 = parseInt(prompt("Podaj współrzędną x:"));
console.log(a2 * x2 + b2);

// c) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = x^3 + 22 - 20$ w tym punkcie.
const x3 = parseInt(prompt("Podaj współrzędną x:"));
console.log(x3 ** 3 + 2);

// d) Pobierz współczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax^m + bx^n + c - d$ w tym punkcie.
const a4 = parseInt(prompt("Podaj współczynnik a:"));
const b4 = parseInt(prompt("Podaj współczynnik b:"));
const c4 = parseInt(prompt("Podaj współczynnik c:"));
const d4 = parseInt(prompt("Podaj współczynnik d:"));
const m4 = parseInt(prompt("Podaj współczynnik m:"));
const n4 = parseInt(prompt("Podaj współczynnik n:"));
const x4 = parseInt(prompt("Podaj współrzędną x:"));
console.log(a4 * x4 ** m4 + b4 * x4 ** n4 + c4 - d4);

// e) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.
const x5 = parseInt(prompt("Podaj współrzędną x:"));
console.log(
  Math.sin(x5) ** 3 * Math.cos(x5) ** 2 +
    Math.E ** (x5 ** 2) +
    Math.log(x5 ** 3 + 2 * x5 ** 2 - x5 - 3)
);
