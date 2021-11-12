"""
Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora dla otrzymanych 
dwoch liczb odpowie na nastepujace pytanie:

a) Czy pierwsza liczba jest wieksza od drugiej liczby?
b) Czy suma liczb jest mniejsza niz 10?
c) Czy obie liczby sa nieparzyste?
d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu?
"""


def pierwsza_wieksza(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba > druga_liczba


def suma_mniejsza_10(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba + druga_liczba < 10


def obie_nieparzyste(pierwsza_liczba, druga_liczba):
    return pierwsza_liczba % 2 != 0 and druga_liczba % 2 != 0


def wieksza_mniejsza_pierwsza_kwadrat(pierwsza_liczba, druga_liczba):
    return max(pierwsza_liczba, druga_liczba) < pierwsza_liczba ** 2


def test_pierwsza_wieksza():
    assert not pierwsza_wieksza(1, 2)
    assert pierwsza_wieksza(2, 1)


def test_suma_mniejsza_10():
    assert suma_mniejsza_10(1, 2)
    assert not suma_mniejsza_10(2, 1)


def test_obie_nieparzyste():
    assert obie_nieparzyste(1, 2)
    assert obie_nieparzyste(2, 1)
    assert not obie_nieparzyste(2, 2)


def test_wieksza_mniejsza_pierwsza_kwadrat():
    assert wieksza_mniejsza_pierwsza_kwadrat(1, 2)
    assert not wieksza_mniejsza_pierwsza_kwadrat(2, 1)
    assert not wieksza_mniejsza_pierwsza_kwadrat(2, 2)


if __name__ == "__main__":

    test_pierwsza_wieksza()
    test_suma_mniejsza_10()
    test_obie_nieparzyste()
    test_wieksza_mniejsza_pierwsza_kwadrat()
