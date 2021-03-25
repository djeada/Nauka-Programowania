"""
Wypisz spiralnie liste dwuwymiarowa.
"""

# Wersja 1
def spiralaV1(macierz, x=0, y=0):

    wynik = []

    if x == 0 and y == 0:
        x, y = len(macierz[0]), len(macierz)

    k = 0
    l = 0

    while k < y and l < x:

        for i in range(l, x):
            wynik.append(macierz[k][i])

        k += 1

        for i in range(k, y):
            wynik.append(macierz[i][x - 1])

        x -= 1

        if k < x:

            for i in range(x - 1, (l - 1), -1):
                wynik.append(macierz[y - 1][i])

            y -= 1

        if l < y:

            for i in range(y - 1, k - 1, -1):
                wynik.append(macierz[i][l])

            l += 1

    return wynik


# Testy Poprawnosci
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

assert spiralaV1(macierz) == wynik
