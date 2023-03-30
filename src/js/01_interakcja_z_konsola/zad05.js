/*
Tytul: Obliczanie wartosci funkcji w danym punkcie.

Tresc zadania: Napisz program, ktory bedzie obliczac wartosc funkcji w danym punkcie zgodnie z nastepujacymi instrukcjami:

a) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = 3x + 10$ w tym punkcie.

b) Pobierz wspolczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie.

c) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym punkcie.

d) Pobierz wspolczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.

e) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.

Dane wejsciowe:

* Liczba naturalna dla punktow 1, 3 i 5.
* Trzy liczby naturalne dla punktu 2.
* Szesc liczb naturalnych dla punktu 4.

Dane wyjsciowe:

* Liczba naturalna dla punktow 1, 2, 3 i 4.
* Liczba zmiennoprzecinkowa dla punktu 5.

Przyklad:

a) Jesli otrzymasz wspolrzedna $x = 3$, program powinien wypisac liczbe 19.

b) Jesli pobierzesz liczby 1, 2 i 3, program powinien wypisac liczbe 5.

c) Jesli otrzymasz wspolrzedna $x = 5$, program powinien wypisac liczbe 155.

d) Jesli pobierzesz liczby 1, 1, 1, 1, 1 i 1, program powinien wypisac liczbe 2.
 
e) Jesli otrzymasz wspolrzedna $x = 2$, program powinien wypisac liczbe 57.179.
*/
// a) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = 3x + 10$ w tym punkcie.
const x1 = parseInt(prompt("Podaj wspolrzedna x:"));
console.log(3 * x1 + 10);

// b) Pobierz wspolczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie.
const a2 = parseInt(prompt("Podaj wspolczynnik a:"));
const b2 = parseInt(prompt("Podaj wspolczynnik b:"));
const x2 = parseInt(prompt("Podaj wspolrzedna x:"));
console.log(a2 * x2 + b2);

// c) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym punkcie.
const x3 = parseInt(prompt("Podaj wspolrzedna x:"));
console.log(x3 ** 3 + 2);

// d) Pobierz wspolczynniki $a$, $b$, $c$, $d$, $m$, $n$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax^m + bx^n + c - d$ w tym punkcie.
const a4 = parseInt(prompt("Podaj wspolczynnik a:"));
const b4 = parseInt(prompt("Podaj wspolczynnik b:"));
const c4 = parseInt(prompt("Podaj wspolczynnik c:"));
const d4 = parseInt(prompt("Podaj wspolczynnik d:"));
const m4 = parseInt(prompt("Podaj wspolczynnik m:"));
const n4 = parseInt(prompt("Podaj wspolczynnik n:"));
const x4 = parseInt(prompt("Podaj wspolrzedna x:"));
console.log(a4 * x4 ** m4 + b4 * x4 ** n4 + c4 - d4);

// e) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.
const x5 = parseInt(prompt("Podaj wspolrzedna x:"));
console.log(
  Math.sin(x5) ** 3 * Math.cos(x5) ** 2 +
    Math.E ** (x5 ** 2) +
    Math.log(x5 ** 3 + 2 * x5 ** 2 - x5 - 3)
);

