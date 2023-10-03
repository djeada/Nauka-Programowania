"""
Tytul: Potega.
Tresc: Otrzymujesz dwie liczby, a i b. Przy uzyciu rekurencji oblicz a podniesione do b.
Dane wejsciowe: Dwie liczby naturalne a i b.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla a = 2 i b = 3, powinna zostac zwrocona liczba: 8.

"""


def potega(a, b):
    """
    Funkcja oblicza a podniesione do b.
    """

    if b < 0:
        return 1 / potega(a, -b)

    if b == 0:
        return 1
    else:
        return a * potega(a, b - 1)


def test_potega():
    assert potega(2, 3) == 8
    assert potega(2, 0) == 1
    assert potega(2, -3) == 0.125


if __name__ == "__main__":
    test_potega()
