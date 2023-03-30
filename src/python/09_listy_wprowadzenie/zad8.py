"""
Tytul: Znalezienie wszystkich par elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz wszystkie pary elementow listy, ktorych suma jest rowna x.
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Lista par liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostana zwrocone wszystkie pary elementow o sumie rownej 5: [(1, 4), (2, 3)].

"""
from math import pow


def usun_klucz(lista, klucz):
    for i in range(len(lista)):
        if lista[i] == klucz:
            lista.pop(i)
            return lista
    return lista


def test_usun_klucz():
    assert usun_klucz([1, 2, 3, 3], 3) == [1, 2, 3]
    assert usun_klucz([1, 2, 3, 3], 4) == [1, 2, 3, 3]
    assert usun_klucz([1, 1, 1, 1], 1) == [1, 1, 1]


if __name__ == "__main__":

    test_usun_klucz()

