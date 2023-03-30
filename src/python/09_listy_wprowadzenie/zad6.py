"""
Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.
Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.

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

