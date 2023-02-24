"""
Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci:

a) Ich sume.
b) Roznice drugiej i pierwszej.
c) Ich iloczyn.
d) Iloraz pierwszej przez druga.
e) Reszte z dzielenia pierwszej przez druga.
"""


def suma(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zwraca sume dwoch liczb.
    '''
    return pierwsza_liczba + druga_liczba


def roznica(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zwraca roznice dwoch liczb.
    '''
    return pierwsza_liczba - druga_liczba


def iloczyn(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zwraca iloczyn dwoch liczb.
    '''
    return pierwsza_liczba * druga_liczba


def iloraz(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zwraca iloraz dwoch liczb.
    '''
    return pierwsza_liczba / druga_liczba


def reszta(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zwraca reszte z dzielenia pierwszej przez druga.
    '''
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
