"""
Tytul: Wypisanie elementow macierzy spiralnie.
Tresc: Otrzymujesz liste list liczb naturalnych. Zbierz elementy otrzymanej macierzy spiralnie i zapisz je w liscie.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostac zwrocona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].

"""


def spirala(macierz):
    """
    Zwraca liste elementow z macierzy zebranych spiralnie.
    """
    lista = []
    k = 0
    while k < len(macierz):
        for i in range(k, len(macierz) - k):
            lista.append(macierz[k][i])
        for i in range(k + 1, len(macierz) - k):
            lista.append(macierz[i][len(macierz) - k - 1])
        for i in range(len(macierz) - k - 2, k - 1, -1):
            lista.append(macierz[len(macierz) - k - 1][i])
        for i in range(len(macierz) - k - 2, k, -1):
            lista.append(macierz[i][k])
        k += 1
    return lista


def test_spirala():
    macierz = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]
    wynik = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    assert spirala(macierz) == wynik


if __name__ == "__main__":

    test_spirala()
