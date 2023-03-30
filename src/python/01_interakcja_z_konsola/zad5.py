"""
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
