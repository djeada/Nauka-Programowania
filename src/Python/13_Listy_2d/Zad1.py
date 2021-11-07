"""
Otrzymujesz dwie liczby, a oraz b. Stworz macierz a identycznych 
wierszy skladajacych sie z liczb od 0 do b.
"""


def stworz_macierz(a, b):
    """	
    Funkcja tworzy macierz o wymiarach a x b. 
    Kazdy wiersz sklada sie z liczb od 0 do b.
    """
    macierz = []
    for i in range(a):
        macierz.append([])
        for j in range(b + 1):
            macierz[i].append(j)
    return macierz


def test_stworz_macierz():
    assert stworz_macierz(2, 3) == [[0, 1, 2], [0, 1, 2]]
    assert stworz_macierz(3, 2) == [[0, 1], [0, 1], [0, 1]]


if __name__ == "__main__":

    test_stworz_macierz()
