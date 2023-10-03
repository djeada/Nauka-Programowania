"""
Tytul: Macierz z identycznymi wierszami, skladajacymi sie z liczb od 0 do b.
Tresc: Otrzymujesz dwie liczby naturalne, a i b. Stworz macierz, skladajaca sie z a identycznych wierszy, ktore skladaja sie z liczb od 0 do b.
Dane wejsciowe: Dwie liczby naturalne, a i b.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona macierz: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

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
