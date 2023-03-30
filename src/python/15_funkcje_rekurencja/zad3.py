"""
Tytul: Silnia.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz silnie z tej liczby.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 3, powinna zostac zwrocona liczba: 6.

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

