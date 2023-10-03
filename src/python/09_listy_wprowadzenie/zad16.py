"""
Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Para liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).

"""


def znajdz_pare(lista, x):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                return i, j
    return -1, -1


def test_znajdz_pare():
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == (0, 8)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22) == (-1, -1)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == (0, 6)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == (-1, -1)


if __name__ == "__main__":

    test_znajdz_pare()
