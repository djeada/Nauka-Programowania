"""
Otrzymujesz liste liczb, kierunek przesuniec (1 odpowiada przesunieciu 
w prawo, a 0 w lewo) oraz liczbe miejsc o jaka maja zostac przesuniete
elementy listy. Przykladowo dla przesuwania w prawo pierwszy element 
trafia na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego. 
Przesun elementy listy w podanym kierunku.
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
