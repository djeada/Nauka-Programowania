"""
Dla otrzymanej listy oraz liczby x, znajdź indeksy pierwszej pary 
elementów listy, których suma jest równa liczbie x. Jeśli w liście 
nie ma takiej pary, zwróć parę (-1, -1).
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
