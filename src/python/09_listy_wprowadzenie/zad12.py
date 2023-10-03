"""
Tytul: Rotacja w lewo/prawo.
Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.
Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

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
