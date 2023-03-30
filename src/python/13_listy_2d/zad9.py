"""
Tytul: Gra w statki
Tresc: Napisz program implementujacy gre w statki.
Stworz macierz o wymiarach 10x10. Wylosuj polozenia statkow i zapisz je w macierzy. Do dyspozycji masz nastepujace statki:
* 1 statek o dlugosci 4
* 2 statki o dlugosci 3
* 3 statki o dlugosci 2
* 5 statkow o dlugosci 1
Kazde pole moze zawierac tylko jeden statek.
Wypisz na standardowe wyjscie plansze zlozona z 10x10 kropek i popros uzytkownika o podanie wspolrzednych. Jesli na podanych przez uzytkownika wspolrzednych znajduje sie statek, zamien kropke na litere o na planszy. W przeciwnym razie, zamien kropke na litere x.
Powtarzaj krok 2, az wszystkie pozycje statkow zostana odkryte przez uzytkownika lub az na planszy pojawi sie 10 liter x. W obu przypadkach zakoncz gre i poinformuj uzytkownika o wyniku.

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

