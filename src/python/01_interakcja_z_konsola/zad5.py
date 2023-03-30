"""
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

"""
import math


if __name__ == "__main__":

    print("podaj x")
    x = int(input())

    print("3*x+10")
    print(3 * x + 10)

    print("podaj a")
    a = int(input())

    print("podaj b")
    b = int(input())

    print("podaj x")
    x = int(input())

    print("a*x+b")
    print(a * x + b)

    print("podaj x")

    x = int(input())

    print("y = x**3 + 2x**2 - 20")
    print(x ** 3 + 2 * x ** 2 - 20)

    print("podaj a")
    a = int(input())

    print("podaj b")
    b = int(input())

    print("podaj c")
    c = int(input())

    print("podaj d")
    d = int(input())

    print("podaj m")
    m = int(input())

    print("podaj n")
    n = int(input())

    print("podaj x")
    x = int(input())

    print("a*x**m + b*x**n + c - a")
    print(a * x ** m + b * x ** n + c - a)

    print("podaj x")

    x = int(input())

    print("sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)")
    print(
        math.sin(3 * x) * math.cos(2 * x)
        + math.exp(x ** 2)
        + math.log(x ** 3 + 2 * x ** 2 - x - 3)
    )

