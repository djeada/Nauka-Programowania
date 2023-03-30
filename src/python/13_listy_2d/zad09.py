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

def znajdz_klepsydry(macierz):
    """
    Przejdz przez macierz i znajdz wszystkie klepsydry.
    """

    # throw exception if not square
    if len(macierz) != len(macierz[0]):
        raise Exception("Macierz nie jest kwadratowa")

    n = len(macierz)

    klepsydry = []
    for wiersz in range(n):
        for kolumna in range(n):
            if not (wiersz == 0 or wiersz == n - 1 or kolumna == 0 or kolumna == n - 1):
                suma = (
                    macierz[wiersz + 1][kolumna]
                    + macierz[wiersz + 1][kolumna - 1]
                    + macierz[wiersz + 1][kolumna + 1]
                )
                suma += macierz[wiersz][kolumna]
                suma += (
                    macierz[wiersz - 1][kolumna]
                    + macierz[wiersz - 1][kolumna - 1]
                    + macierz[wiersz - 1][kolumna + 1]
                )
                klepsydry.append(suma)

    return klepsydry

def najwieksza_klepsydra(macierz):
    return max(znajdz_klepsydry(macierz))

def test_najwieksza_klepsydra():

    macierz = [
        [10, 99, 28, 21, 78],
        [35, 78, 31, 56, 24],
        [7, 18, 2, 50, 87],
        [59, 67, 9, 82, 53],
        [23, 26, 76, 62, 36],
    ]
    assert najwieksza_klepsydra(macierz) == 395

if __name__ == "__main__":

    test_najwieksza_klepsydra()

