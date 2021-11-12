"""
Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca sie 
z liczby kolumn i wierszy rownej otrzymanej liczbie, ktorej kazdy 
element jest iloczynem jego wspolrzednych.
"""


def stworz_macierz(n):
    """
    Funkcja tworzy macierz o wymiarach n x n, dla ktorej kazdy 
    element jest rowny iloczynowi wspolrzednych.
    """
    macierz = []
    for i in range(n):
        macierz.append([])
        for j in range(n):
            macierz[i].append(i * j)
    return macierz


def test_stworz_macierz():
    assert stworz_macierz(3) == [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
    assert stworz_macierz(4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]


if __name__ == "__main__":

    test_stworz_macierz()
