"""
Tytul: Klepsydra o najwiekszej sumie.
Tresc: Otrzymasz liste list liczb naturalnych. Znajdz w macierzy klepsydre o najwiekszej sumie. Klepsydra sklada sie dokladnie z 7 elementow. Pierwsze trzy elementy sa kolejnymi elementami dowolnego wiersza macierzy. Czwarty element znajduje sie w tej samej kolumnie co drugi element i o jeden wiersz nizej. Ostatnie trzy elementy znajduja sie w tych samych kolumnach co trzy pierwsze i o dwa wiersze nizej.
Podpowiedz: Nastepujaca macierz:
1 2 3
4 5 6
7 8 9
ma tylko jedna klepsydre:
1 2 3
5
7 8 9
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19, 14]], powinna zostac zwrocona liczba: 75.

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

