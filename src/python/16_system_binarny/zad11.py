"""
Tytul: Operacje arytmetyczne.
Tresc: Otrzymujesz dwie liczby naturalne. Uzywajac jedynie operatorow bitowych, zaimplementuj:
a) Dodawanie.
b) Odejmowanie.
c) Mnozenie.
d) Dzielenie.
Dane wejsciowe: Dwie liczby naturalne w kazdym podpunkcie.
Dane wyjsciowe: Liczba naturalna w kazdym podpunkcie.
Przyklad:
a) Dla otrzymanych liczb: 2 i 3, powinna zostac zwrocona liczba: 5.
b) Dla otrzymanych liczb: 7 i 5, powinna zostac zwrocona liczba: 2.
c) Dla otrzymanych liczb: 4 i 4, powinna zostac zwrocona liczba: 16.
d) Dla otrzymanych liczb: 9 i 3, powinna zostac zwrocona liczba: 3.

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

