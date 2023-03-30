"""
Tytul:  Sprawdz warunek
Napisz funkcje, ktora sprawdzi nastepujace warunki dla otrzymanych dwoch liczb:
a) Czy pierwsza liczba jest wieksza od drugiej liczby?
b) Czy suma liczb jest mniejsza niz 10?
c) Czy obie liczby sa nieparzyste?
d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu?
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: cztery wartosci logiczne, odpowiadajace na kazde z pytan
Przyklad:
Dla pobranych liczb 3 i 2, funkcja powinna zwrocic nastepujace wartosci logiczne:
a) Prawda
b) Prawda
c) Falsz
d) Prawda

"""


def pierwsza_wieksza(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy pierwsza liczba jest wieksza od drugiej liczby.
    """
    return pierwsza_liczba > druga_liczba


def suma_mniejsza_10(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy suma liczb jest mniejsza niz 10.
    """
    return pierwsza_liczba + druga_liczba < 10


def obie_nieparzyste(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy obie liczby sa nieparzyste.
    """
    return pierwsza_liczba % 2 != 0 and druga_liczba % 2 != 0


def wieksza_mniejsza_pierwsza_kwadrat(pierwsza_liczba, druga_liczba):
    """
    Funkcja sprawdza czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu.
    """
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

