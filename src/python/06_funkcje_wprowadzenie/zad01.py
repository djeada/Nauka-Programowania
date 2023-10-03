"""
Tytul: Zwroc stala.
Tresc: Napisz funkcje, ktora zwroci:
a) Liczbe 3.
b) Napis "Tak".
c) Wartosc logiczna Prawda.
Dane wejsciowe: Brak.
Dane wyjsciowe:
a) Liczba 3.
b) Napis "Tak".
c) Wartosc logiczna Prawda.

"""


def zwroc_3():
    """
    Funkcja zwraca liczbe 3.
    """
    return 3


def zwroc_tak():
    """
    Funkcja zwraca napis "Tak".
    """
    return "Tak"


def zwroc_prawda():
    """
    Funkcja zwraca wartosc logiczna Prawda.
    """
    return True


def test_zwroc_3():
    assert zwroc_3() == 3


def test_zwroc_tak():
    assert zwroc_tak() == "Tak"


def test_zwroc_prawda():
    assert zwroc_prawda() == True


if __name__ == "__main__":

    test_zwroc_3()
    test_zwroc_tak()
    test_zwroc_prawda()
