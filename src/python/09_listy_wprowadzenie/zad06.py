"""
Tytul: Czy srednia elementow znajduje sie w liscie?
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.
Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.
Przyklad:
Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

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
