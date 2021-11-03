"""
Otrzymujesz listę list liczb naturalnych. Znajdź w macierzy klepsydrę o największej sumie. 
Klepsydra składa się z dokładnie 7 elementów. Trzy pierwsze elementy są kolejnymi 
elementami dowolnego wiersza macierzy. Następny element znajduje się w tej samej
kolumnie co drugi element i w dokładnie jednym wierszu niżej. Trzy następne znajdują się 
w tych samych kolumnach co trzy pierwsze i dokładnie dwa wiersze niżej.
"""

def znajdz_klepsydry(macierz):
    '''
    Przejdz przez macierz i znajdz wszystkie klepsydry.
    '''

    # throw exception if not square
    if len(macierz) != len(macierz[0]):
        raise Exception("Macierz nie jest kwadratowa")

    n = len(macierz)

    klepsydry = []
    for wiersz in range(n):
        for kolumna in range(n):
            if not (wiersz == 0 or wiersz == n - 1 or kolumna == 0 or kolumna == n - 1):
                suma = macierz[wiersz + 1][kolumna] + macierz[wiersz + 1][kolumna - 1]  + macierz[wiersz + 1][kolumna + 1] 
                suma += macierz[wiersz][kolumna]
                suma += macierz[wiersz - 1][kolumna] + macierz[wiersz - 1][kolumna - 1] + macierz[wiersz - 1][kolumna + 1]
                klepsydry.append(suma)

    return klepsydry

def najwieksza_klepsydra(macierz):
    return max(znajdz_klepsydry(macierz))


def test_najwieksza_klepsydra():

    macierz = [[10, 99, 28, 21, 78], [35, 78, 31, 56, 24], [7, 18, 2, 50, 87], [59, 67, 9, 82, 53], [23, 26, 76, 62, 36]]
    assert najwieksza_klepsydra(macierz) == 395

if __name__ == "__main__":

    test_najwieksza_klepsydra() 