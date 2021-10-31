"""
Pobierz dwie liczby od użytkownika. Napisz funkcję, która dla otrzymanych dwóch liczb zwróci:

a) Ich sumę.
b) Różnicę drugiej i pierwszej.
c) Ich iloczyn.
d) Iloraz pierwszej przez drugą.
e) Resztę z dzielenia pierwszej przez drugą.
"""


def suma(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba


def roznica(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba - druga_liczba


def iloczyn(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba * druga_liczba


def iloraz(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba / druga_liczba


def reszta(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba % druga_liczba


def test_suma():
    assert suma(2, 3) == 5


def test_roznica():
    assert roznica(2, 3) == -1


def test_iloczyn():
    assert iloczyn(2, 3) == 6


def test_iloraz():
    assert iloraz(9, 3) == 3


def test_reszta():
    assert reszta(9, 3) == 0


if __name__ == "__main__":

    test_suma()
    test_roznica()
    test_iloczyn()
    test_iloraz()
    test_reszta()
