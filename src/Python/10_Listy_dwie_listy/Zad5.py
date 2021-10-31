"""
Otrzymujesz dwie listy liczb zmiennoprzecinkowych, pierwsza 
reprezentuje wagi, a druga wartosci. Oblicz srednia wazona wartosci.
"""


def srednia_wazona(wartosci, wagi):

    if len(wartosci) != len(wagi):
        raise ValueError("Listy roznej dlugosci")

    suma = 0
    for waga, wartosc in zip(wagi, wartosci):
        suma += waga * wartosc

    return suma / sum(wartosci)


def test_srednia_wazona():
    assert srednia_wazona([1, 2, 3], [1, 1, 1]) == 1
    assert srednia_wazona([0, -23, -5, 2, -3, 4, 9], [1, 2, 3, 4, 5, 6, 7]) == -1.1875


if __name__ == "__main__":
    test_srednia_wazona()
