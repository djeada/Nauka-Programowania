"""
Otrzymujesz liste liczb naturalnych. Sprawdz czy srednia elementow 
listy znajduje sie w liscie. Dla sredniej nie bedacej liczba calkowita, 
zaokraglij wynik w dol.
"""


def czy_srednia_w_liscie(lista):

    if not lista:
        return False

    srednia = sum(lista) / len(lista)

    if srednia.is_integer():
        return srednia in lista
    else:
        return round(srednia, 0) in lista


def test_czy_srednia_w_liscie_dla_pustej_listy():
    assert not czy_srednia_w_liscie([])
    assert czy_srednia_w_liscie([1, 2, 3])
    assert czy_srednia_w_liscie([-5, 7, 2, 3, -1, 4])


if __name__ == "__main__":

    test_czy_srednia_w_liscie_dla_pustej_listy()
