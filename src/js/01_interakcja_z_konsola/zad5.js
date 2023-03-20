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
var x = parseInt(prompt("Podaj współrzędną x:"));
console.log(3 * x + 10);

// b) Pobierz współczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax + b$ w tym punkcie.
var a = parseInt(prompt("Podaj współczynnik a:"));
var b = parseInt(prompt("Podaj współczynnik b:"));
var x = parseInt(prompt("Podaj współrzędną x:"));
console.log(a * x + b);

// c) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = x^3 + 22 - 20$ w tym punkcie.
var x = parseInt(prompt("Podaj współrzędną x:"));
console.log(x ** 3 + 22 - 20);

// d) Pobierz współczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartość funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.
var a = parseInt(prompt("Podaj współczynnik a:"));
var b = parseInt(prompt("Podaj współczynnik b:"));
var c = parseInt(prompt("Podaj współczynnik c:"));
var d = parseInt(prompt("Podaj współczynnik d:"));
var m = parseInt(prompt("Podaj współczynnik m:"));
var n = parseInt(prompt("Podaj współczynnik n:"));
var x = parseInt(prompt("Podaj współrzędną x:"));
console.log(a * x ** m + b * x ** n + c - d);

// e) Otrzymujesz współrzędną $x$. Wyznacz wartość funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.
var x = parseInt(prompt("Podaj współrzędną x:"));
console.log(Math.sin(x) ** 3 * Math.cos(x) ** 2 + Math.E ** (x ** 2) + Math.log(x ** 3 + 2 * x ** 2 - x - 3));