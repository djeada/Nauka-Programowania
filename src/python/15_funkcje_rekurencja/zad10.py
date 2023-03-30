"""
Tytul: Suma liczb naturalnych mniejszych od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz sume liczb naturalnych mniejszych od N.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 10, powinna zostac zwrocona liczba: 55.

"""


def gra(n):
    """
    Funkcja zwraca liczbe sposobow na wygrana w grze.
    """

    if n < min(3, 5, 10):
        return 0

    lista_wynikow = []

    def _gra(n, wynik=[]):
        """
        Wewnetrzna funkcja rekurencyjna.
        """

        if n < 0:
            return 0

        if n == 0:
            if sorted(wynik) not in lista_wynikow:
                lista_wynikow.append(wynik)
                return 1
            return 0

        return (
            _gra(n - 3, wynik + [3])
            + _gra(n - 5, wynik + [5])
            + _gra(n - 10, wynik + [10])
        )

    return _gra(n)


def test_gra():

    assert gra(20) == 4
    assert gra(10) == 2
    assert gra(50) == 14
    assert gra(1) == 0


if __name__ == "__main__":

    test_gra()

