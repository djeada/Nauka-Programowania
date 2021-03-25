"""
Znajdz w macierzy klepsydre o najwiekszej sumie.
"""

# Wersja 1
def maks_klepsydra(macierz):
    maks = -float("Inf")

    N = len(macierz)

    for wiersz in range(N):
        for kolumna in range(N):
            if not (wiersz == 0 or wiersz == N - 1 or kolumna == 0 or kolumna == N - 1):
                maks = max(
                    maks,
                    (
                        macierz[wiersz - 1][kolumna - 1]
                        + macierz[wiersz - 1][kolumna]
                        + macierz[wiersz - 1][kolumna + 1]
                        + macierz[wiersz][kolumna]
                        + macierz[wiersz + 1][kolumna - 1]
                        + macierz[wiersz + 1][kolumna]
                        + macierz[wiersz + 1][kolumna + 1]
                    ),
                )

    return maks


# Testy Poprawnosci
def test_1():
    macierz = [
        [10, 99, 28, 21, 78],
        [35, 78, 31, 56, 24],
        [7, 18, 2, 50, 87],
        [59, 67, 9, 82, 53],
        [23, 26, 76, 62, 36],
    ]

    wynik = 395
    assert maks_klepsydra(macierz) == wynik


test_1()
