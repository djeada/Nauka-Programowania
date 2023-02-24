import math

"""
Napisz funkcje, ktora dla otrzymanej liczby sprawdzi czy jest ona liczba pierwsza.
"""


def podziel(a, b):

    znak = 1

    if b == 0:
        return float("nan")

    if a == 0:
        return 0

    if a < 0:
        znak = -1
        a = -a

    if b < 0:
        znak *= -1
        b = -b

    if znak == 1:
        licznik = 0
        while a >= b:
            a -= b
            licznik += 1

    else:
        licznik = 1
        while a > b:
            a -= b
            licznik += 1

    return licznik * znak


def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(10, 3) == 3
    assert podziel(25, -5) == -5
    assert podziel(-25, 5) == -5
    assert podziel(-25, -5) == 5
    assert podziel(0, 5) == 0
    assert math.isnan(podziel(0, 0))


if __name__ == "__main__":

    test_podziel()
