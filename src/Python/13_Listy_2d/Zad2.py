"""
Dla otrzymanej liczby, stwórz macierz kwadratową składającą się 
z liczby kolumn i wierszy równej otrzymanej liczbie, której każdy 
element jest iloczynem jego współrzędnych.
"""

def stworz_macierz(n):
    """
    Funkcja tworzy macierz o wymiarach n x n, dla której każdy 
    element jest równy iloczynowi współrzędnych.
    """
    macierz = []
    for i in range(n):
        macierz.append([])
        for j in range(n):
            macierz[i].append(i*j)
    return macierz

def test_stworz_macierz():
    assert stworz_macierz(3) == [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
    assert stworz_macierz(4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]


if __name__ == "__main__":

    test_stworz_macierz()

