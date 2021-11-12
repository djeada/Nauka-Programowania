"""
Napisz funkcje, ktora przy pomocy petli obliczy silnie 
otrzymanej liczby.
"""


def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 120


if __name__ == "__main__":

    test_silnia()
