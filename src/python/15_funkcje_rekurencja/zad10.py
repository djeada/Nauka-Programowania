"""
Rozwaz gre, w ktorej w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. 
Dla otrzymanej liczby N, reprezentujacej calkowita liczbe punktow, 
oblicz na ile sposobow gracz moze wygrac gre.
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
