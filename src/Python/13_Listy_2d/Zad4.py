"""
Otrzymujesz dwie macierze o tych samych wymiarach, zwróć macierz będącą:

a) Wynikiem dodawania otrzymanych macierzy.
b) Wynikiem odejmowania pierwszej macierzy od drugiej.
"""

def suma_macierzy(macierz_a, macierz_b):
    """	
    Funkcja sumuje dwie macierze o rownych wymiarach i zwraca wynik.
    """

    if len(macierz_a) != len(macierz_b):
        raise ValueError("Macierze mają różne wymiary!")
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
        raise ValueError("Macierze mają różne wymiary!")
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