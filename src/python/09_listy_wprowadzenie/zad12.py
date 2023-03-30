"""
Tytul: Minimum oraz maksimum.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy element tej listy i zwroc je jako dwie osobne liczby calkowite.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Dwie liczby calkowite oznaczajace najwiekszy i najmniejszy element z listy.
Przyklad:
Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.

"""


def rotacja(lista, kierunek, miejsce):
    if kierunek == 1:
        for _ in range(miejsce):
            lista.insert(0, lista.pop())
    else:
        for _ in range(miejsce):
            lista.append(lista.pop(0))

    return lista


def test_rotacja():
    assert rotacja([1, 2, 3, 4, 5], 1, 2) == [4, 5, 1, 2, 3]
    assert rotacja([5, 27, 6, 2, 1, 10, 8], 0, 2) == [6, 2, 1, 10, 8, 5, 27]
    assert rotacja([9, 9, 42, 47, 5, 6, 19, 7], 1, 3) == [6, 19, 7, 9, 9, 42, 47, 5]


if __name__ == "__main__":

    test_rotacja()

