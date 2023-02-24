"""
Otrzymujesz liste n wspolczynnikow wielomianu postaci: a_nx^n + a_(n-1)x^(n-1) + ... + a_0
oraz liczbe naturalna x. Znajdz wartosc wielomianu w zadanym punkcie.
"""


def wartosc_wielomianu_w_punkcie(wspolczynniki, x):
    """
    Funkcja zwraca wartosc wielomianu w punkcie x.
    """
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik += wspolczynniki[i] * x ** i
    return wynik


def test_wartosc_wielomianu_w_punkcie():
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 2) == 49
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 3) == 142


if __name__ == "__main__":
    test_wartosc_wielomianu_w_punkcie()
