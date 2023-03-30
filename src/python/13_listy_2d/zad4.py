"""
Tytul: Scalanie przedzialow w liscie przedzialow.
Tresc: Otrzymujesz liste par liczb. Kazda para reprezentuje poczatek i koniec przedzialu. Niektore przedzialy moga sie nachodzic. W takim przypadku polacz je ze soba i zwroc liste przedzialow, ktore sie nie pokrywaja.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej listy: [[23, 67], [23, 53], [45, 88], [77, 88], [10, 22], [11, 12], [42, 45]], powinna zostac zwrocona lista: [[10, 22], [23, 88]].

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

