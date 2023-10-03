"""
Tytul: Suma liczb naturalnych mniejszych od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz sume liczb naturalnych mniejszych od N.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 10, powinna zostac zwrocona liczba: 55.

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
