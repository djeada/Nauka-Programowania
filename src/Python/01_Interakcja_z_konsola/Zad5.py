import math

"""
Wyznacz wartość funkcji w punkcie:

a) Otrzymujesz współrzędną x. Wyznacz wartość funkcji y = 3x + 10 w zadanym punkcie.
b) Pobierz współczynniki a, b oraz punkt x. Wyznacz wartość funkcji y = ax + b w zadanym punkcie.
c) Otrzymujesz współrzędną x. Wyznacz wartość funkcji y = x3 + 22 - 20 w zadanym punkcie.
d) Pobierz współczynniki a, b, c, d, m, n oraz punkt x. Wyznacz wartość funkcji y = a*xm + b*xn + c - a w zadanym punkcie.
e) Otrzymujesz współrzędną x. Wyznacz wartość funkcji y = sin3x*cos2x + ex2 + log(x3+2x2-x-3) w zadanym punkcie.
"""

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
