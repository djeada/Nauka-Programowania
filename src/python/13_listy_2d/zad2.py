"""
Tytul: Dodawanie i odejmowanie macierzy.
Tresc: Otrzymujesz dwie macierze o tych samych wymiarach. Zwroc dwie macierze bedace:
a) wynikiem dodawania otrzymanych macierzy
b) wynikiem odejmowania drugiej macierzy od pierwszej.
Dane wejsciowe: Dwie listy list liczb naturalnych.
Dane wyjsciowe: Dwie listy list liczb naturalnych.
Przyklad:
Dla otrzymanych dwoch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinny zostac zwrocone nastepujace macierze:
a) [[6, -1], [-1, 7]] - wynik dodawania
b) [[-4, 5], [-3, -7]] - wynik odejmowania drugiej macierzy od pierwszej.

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

