"""
Tytul: Cyfry liczby
Tresc: Napisz funkcje, ktora dla otrzymanej liczby obliczy sume jej cyfr.
Dane wejsciowe: liczba naturalna
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranej liczby 13231, funkcja powinna zwrocic liczbe 10.

"""

def suma_cyfr(liczba):
    """
    Funkcja zwraca sume cyfr podanej liczby.
    """
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma

def test_suma_cyfr_dla_liczby_123():
    assert suma_cyfr(123) == 6

def test_suma_cyfr_dla_liczby_0():
    assert suma_cyfr(0) == 0

if __name__ == "__main__":

    test_suma_cyfr_dla_liczby_0()
    test_suma_cyfr_dla_liczby_123()

