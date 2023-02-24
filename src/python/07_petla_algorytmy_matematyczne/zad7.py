"""
Napisz funkcje, ktora dla otrzymanej liczby zwroci jej pierwiastek.
"""

dokladnosc = 0.0001


def pierwiastek(liczba):

    wynik = liczba

    while abs(liczba - wynik * wynik) > dokladnosc:
        wynik = (wynik + liczba / wynik) / 2

    return wynik


def test_pierwiastek():
    assert abs(pierwiastek(1) - 1) < dokladnosc
    assert abs(pierwiastek(4) - 2) < dokladnosc
    assert abs(pierwiastek(9) - 3) < dokladnosc


if __name__ == "__main__":

    test_pierwiastek()
