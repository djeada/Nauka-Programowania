"""
Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem rekurencyjnym:
a_1 = 1,
a_n = 1 + 2a_(n-1)
"""


def wyraz_ciag(n):
    """
    Funkcja oblicza n-ty wyraz ciagu danego wzorem rekurencyjnym: 
    a_1 = 1,
    a_n = 1 + 2a_(n-1)
    """
    if n < 1:
        raise ValueError("Liczba musi byc wieksza od zera")

    if n == 1:
        return 1
    else:
        return 1 + 2 * wyraz_ciag(n - 1)


def test_wyraz_ciag():

    assert wyraz_ciag(1) == 1
    assert wyraz_ciag(2) == 3
    assert wyraz_ciag(10) == 1023


if __name__ == "__main__":
    test_wyraz_ciag()
