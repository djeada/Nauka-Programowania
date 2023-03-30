"""
Tytul: Potega.
Tresc: Otrzymujesz dwie liczby, a i b. Przy uzyciu rekurencji oblicz a podniesione do b.
Dane wejsciowe: Dwie liczby naturalne a i b.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla a = 2 i b = 3, powinna zostac zwrocona liczba: 8.

"""

def suma_liczb_mniejszych_niz_n(n):
    """
    Funkcja oblicza sume liczb mniejszych od podanej liczby n.
    """

    if n < 1:
        return 0

    if n == 1:
        return 1

    return n + suma_liczb_mniejszych_niz_n(n - 1)

def test_suma_liczb_mniejszych_niz_n():

    assert suma_liczb_mniejszych_niz_n(1) == 1

if __name__ == "__main__":

    test_suma_liczb_mniejszych_niz_n()

