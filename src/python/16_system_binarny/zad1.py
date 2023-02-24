"""
a) Otrzymujesz dziesietna reprezentacje liczby naturalnej, zwroc jej binarna reprezentacje.
b) Otrzymujesz binarna reprezentacje liczby naturalnej, zwroc jej dziesietna reprezentacje.
"""


def na_dziesietny(liczba):
    """
    Funkcja zamienia liczbe binarna na dziesietna.
    """
    wynik = 0
    for pozycja, cyfra in enumerate(liczba[::-1]):
        wynik += (2 ** int(pozycja)) * int(cyfra)

    return wynik


def na_binarny(liczba):
    """
    Funkcja zamienia liczbe dziesietna na binarna.
    """
    if liczba == 0:
        return "0"

    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 2) + wynik
        liczba = liczba // 2

    return wynik


def test_na_dziesietny():
    assert na_dziesietny("101") == 5
    assert na_dziesietny("1101") == 13
    assert na_dziesietny("1111") == 15


def test_na_binarny():
    assert na_binarny(5) == "101"
    assert na_binarny(13) == "1101"
    assert na_binarny(15) == "1111"


if __name__ == "__main__":
    test_na_dziesietny()
    test_na_binarny()
