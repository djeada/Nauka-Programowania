"""
Tytul: Zerowanie macierzy.
Tresc: Otrzymujesz liste list liczb naturalnych reprezentujaca macierz. Jesli element macierzy jest rowny zero, zamien wszystkie elementy tej samej kolumny i wiersza na zera.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Lista list liczb naturalnych.
Przyklad:
Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostac zwrocona macierz: [[1,0,3], [0,0,0], [7,0,9]].

"""

def wyzeruj_macierz(macierz):
    """
    Funkcja zamienia wszystkie elementy w kolumnach i wierszach na zera
    jesli jeden z elementow jest rowny zero.
    """
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 0:
                for k in range(len(macierz)):
                    macierz[i][k] = 0
                    macierz[k][j] = 0
    return macierz

def test_wyzeruj_macierz():
    assert wyzeruj_macierz([[1, 2, 3], [4, 0, 6], [7, 8, 9]]) == [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9],
    ]
    assert wyzeruj_macierz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

if __name__ == "__main__":

    test_wyzeruj_macierz()

