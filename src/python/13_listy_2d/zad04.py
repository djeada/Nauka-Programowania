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

def suma_macierzy(macierz_a, macierz_b):
    """
    Funkcja sumuje dwie macierze o rownych wymiarach i zwraca wynik.
    """

    if len(macierz_a) != len(macierz_b):
        raise ValueError("Macierze maja rozne wymiary!")
    macierz_c = []
    for i in range(len(macierz_a)):
        macierz_c.append([])
        for j in range(len(macierz_a[i])):
            macierz_c[i].append(macierz_a[i][j] + macierz_b[i][j])
    return macierz_c

def roznica_macierzy(macierz_a, macierz_b):
    """
    Funkcja odejmuje macierz_a od macierz_b i zwraca wynik.
    """

    if len(macierz_a) != len(macierz_b):
        raise ValueError("Macierze maja rozne wymiary!")
    macierz_c = []
    for i in range(len(macierz_a)):
        macierz_c.append([])
        for j in range(len(macierz_a[i])):
            macierz_c[i].append(macierz_a[i][j] - macierz_b[i][j])
    return macierz_c

def test_suma_macierzy():
    macierz_a = [[1, 2], [3, 4]]
    macierz_b = [[5, 6], [7, 8]]
    macierz_c = [[6, 8], [10, 12]]
    assert suma_macierzy(macierz_a, macierz_b) == macierz_c

def test_roznica_macierzy():
    macierz_a = [[1, 2], [3, 4]]
    macierz_b = [[5, 6], [7, 8]]
    macierz_c = [[-4, -4], [-4, -4]]
    assert roznica_macierzy(macierz_a, macierz_b) == macierz_c

if __name__ == "__main__":
    test_roznica_macierzy()

