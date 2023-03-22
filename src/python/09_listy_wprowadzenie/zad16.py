"""
Dla otrzymanej listy oraz liczby x, znajdz indeksy pierwszej pary 
elementow listy, ktorych suma jest rowna liczbie x. Jesli w liscie 
nie ma takiej pary, zwroc pare (-1, -1).
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