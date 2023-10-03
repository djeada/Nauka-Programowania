"""
Tytul: Obliczenie n-tej pochodnej wielomianu.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna k. Oblicz wspolczynniki wielomianu bedacego k-ta pochodna otrzymanego wielomianu.
Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla otrzymanej listy wspolczynnikow [4, -3, 2] i liczby k = 1, zostanie zwrocona lista [8, -3].

"""


def pochodna(wielomian, k):
    """
    Funkcja oblicza k-ta pochodna wielomianu.
    """
    wynik = []
    kopia = wielomian[:]

    for i in range(k):
        wynik = []
        n = len(kopia)
        for i in range(n - 1):
            wynik.append(kopia[i] * (n - i - 1))
        kopia = wynik[:]

    return wynik


def test_pochodna():
    assert pochodna([4, -3, 2], 1) == [8, -3]
    assert pochodna([13, -6, 0, -1, -1], 2) == [156, -36, 0]


if __name__ == "__main__":

    test_pochodna()
