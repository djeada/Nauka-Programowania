"""
Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.
"""


def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


def test_suma_cyfr_dla_liczby_123():
    assert suma_cyfr(123) == 6


def test_suma_cyfr_dla_liczby_0():
    assert suma_cyfr(0) == 0


if __name__ == "__main__":

    test_suma_cyfr_dla_liczby_0()
    test_suma_cyfr_dla_liczby_123()
