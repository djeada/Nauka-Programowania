"""
Tytul: Minimum oraz maksimum.
Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy element tej listy i zwroc je jako dwie osobne liczby calkowite.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Dwie liczby calkowite oznaczajace najwiekszy i najmniejszy element z listy.
Przyklad:
Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.

"""

def znajdz_maks(lista):
    maks = lista[0]
    for i in lista:
        if i > maks:
            maks = i
    return maks

def znajdz_min(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min

def test_znajdz_maks():
    assert znajdz_maks([5, 4, 3, 2, 1]) == 5
    assert znajdz_maks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10

def test_znajdz_min():
    assert znajdz_min([5, 4, 3, 2, 1]) == 1
    assert znajdz_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1

if __name__ == "__main__":

    test_znajdz_maks()
    test_znajdz_min()

