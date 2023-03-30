"""
Tytul: Zaokraglanie w dol.
Tresc: Napisz funkcje, ktora zaokragli iloraz dwoch liczb naturalnych do najblizszej liczby calkowitej w dol, bez uzycia operatorow '/' i '%'.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 7 i 2, funkcja powinna zwrocic liczbe 3.

"""
import random


def podziel(a, b):
    """
    Funkcja zwraca iloraz a przez b.
    """
    znak = 1

    if b == 0:
        return float("nan")

    if a == 0:
        return 0

    if a < 0:
        znak = -1
        a = -a

    if b < 0:
        znak *= -1
        b = -b

    if znak == 1:
        licznik = 0
        while a >= b:
            a -= b
            licznik += 1

    else:
        licznik = 1
        while a > b:
            a -= b
            licznik += 1

    return licznik * znak


def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(10, 3) == 3
    assert podziel(25, -5) == -5
    assert podziel(-25, 5) == -5
    assert podziel(-25, -5) == 5
    assert podziel(0, 5) == 0
    assert podziel(0, 0) == float("nan")


if __name__ == "__main__":
    test_podziel()

