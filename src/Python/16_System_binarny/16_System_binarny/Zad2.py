"""
Otrzymujesz liczbe naturalna. Zwroc binarna 
reprezentacje otrzymanej liczby jesli:

a) Otrzymana liczba jest liczba parzysta.
b) Otrzymana liczba jest liczba pierwsza.
"""


def czy_parzysta(n):
    """
    Funkcja sprawdza czy liczba jest parzysta.
    """
    return n % 2 == 0


def czy_pierwsza(n):
    """
    Funkcja sprawdza czy liczba jest pierwsza.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


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


def zamien_liczbe_parzysta(liczba):
    """
    Funkcja zamienia liczbe parzysta na liczbe binarna.
    """
    if czy_parzysta(liczba):
        return na_binarny(liczba)

    return ""


def zamien_liczbe_pierwsza(liczba):
    """
    Funkcja zamienia liczbe pierwsza na liczbe binarna.
    """
    if czy_pierwsza(liczba):
        return na_binarny(liczba)

    return ""


def test_zamien_liczbe_parzysta():

    assert zamien_liczbe_parzysta(0) == "0"
    assert zamien_liczbe_parzysta(1) == ""
    assert zamien_liczbe_parzysta(2) == "10"
    assert zamien_liczbe_parzysta(3) == ""
    assert zamien_liczbe_parzysta(4) == "100"


def test_zamien_liczbe_pierwsza():

    assert zamien_liczbe_pierwsza(0) == ""
    assert zamien_liczbe_pierwsza(1) == ""
    assert zamien_liczbe_pierwsza(2) == "10"
    assert zamien_liczbe_pierwsza(3) == "11"
    assert zamien_liczbe_pierwsza(4) == ""


if __name__ == "__main__":

    test_zamien_liczbe_parzysta()
    test_zamien_liczbe_pierwsza()
