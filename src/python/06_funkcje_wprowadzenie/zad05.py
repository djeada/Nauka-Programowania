"""
Tytul: Zamien wartosci miejscami.
Tresc: Napisz funkcje, ktora zamieni wartosci zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywac wartosc zmiennej b, a zmienna b powinna przechowywac wartosc zmiennej a.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla otrzymanych liczb: 8 i 5, powinny zostac zwrocone liczby 5 i 8.

"""


def swap(pierwsza_liczba, druga_liczba):
    """
    Funkcja zamienia wartosci miejscami.
    """
    return druga_liczba, pierwsza_liczba


def test_swap():
    a, b = 1, 2
    a, b = swap(a, b)
    assert a == 2 and b == 1


if __name__ == "__main__":
    test_swap()
