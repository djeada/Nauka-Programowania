"""
Sprawdz czy binarna reprezentacja liczby jest palindromem.
"""


def czyPalindromV1(liczba):

    odwrocona = 0

    k = liczba
    while k > 0:
        odwrocona = (odwrocona << 1) | (k & 1)
        k >>= 1

    return odwrocona == liczba


if __name__ == "__main__":

    liczba = 0b11011

    assert czyPalindromV1(liczba)

    liczba = 0b1001101

    assert not czyPalindromV1(liczba)
