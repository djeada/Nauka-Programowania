"""
Otrzymujesz dziesietna reprezentacje liczby naturalnej. 
Sprawdz czy binarna reprezentacja otrzymanej liczby jest palindromem.
"""


def czy_palindrom(liczba):
    """
    Funkcja sprawdza czy podana liczba jest palindromem.
    """

    odwrocona = 0

    k = liczba
    while k > 0:
        odwrocona = (odwrocona << 1) | (k & 1)
        k >>= 1

    return odwrocona == liczba


def test_czy_palindrom():

    assert czy_palindrom(0)
    assert czy_palindrom(27)
    assert not czy_palindrom(2)
    assert not czy_palindrom(77)


if __name__ == "__main__":

    test_czy_palindrom()
