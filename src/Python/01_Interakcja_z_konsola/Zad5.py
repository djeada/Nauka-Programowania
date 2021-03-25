import math

if __name__ == "__main__":

    """
    Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.
    """
    print("podaj x")
    x = int(input())

    print("3*x+10")
    print(3 * x + 10)

    """
	Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w zadanym punkcie.
	"""

    print("podaj a")
    a = int(input())

    print("podaj b")
    b = int(input())

    print("podaj x")
    x = int(input())

    print("a*x+b")
    print(a * x + b)

    """
	Wyznacz wartosc funkcji y = x^3 + 2x^2 - 20 w zadanym punkcie.
	"""

    print("podaj x")

    x = int(input())

    print("y = x**3 + 2x**2 - 20")
    print(x ** 3 + 2 * x ** 2 - 20)

    """
	Pobierz wspolczynniki a, b, c, d, m, n oraz punkt x i wyznacz wartosc funkcji y = a*x^m + b*x^n + c - a w zadanym punkcie.
	"""

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

    """
	Wyznacz wartosc funkcji y = sin3x*cos2x + e^x^2 + log(x^3+2x^2-x-3) w zadanym punkcie.
	"""

    print("podaj x")

    x = int(input())

    print("sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)")
    print(
        math.sin(3 * x) * math.cos(2 * x)
        + math.exp(x ** 2)
        + math.log(x ** 3 + 2 * x ** 2 - x - 3)
    )
