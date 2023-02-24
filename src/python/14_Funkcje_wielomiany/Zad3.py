"""
Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci a_nx^n + a_(n-1)x^(n-1) + ... + a_0.
Oblicz wspolczynniki wielomianu bedacego suma otrzymanych wielomianow.
"""


def suma_wielomianow(wielomian_a, wielomian_b):
    """
    Funkcja sumuje dwie listy wielomianow.
    """
    min_dlugosc = min(len(wielomian_a), len(wielomian_b))

    wynik = [wielomian_a[i] + wielomian_b[i] for i in range(min_dlugosc)]

    for i in range(min_dlugosc, len(wielomian_a)):
        wynik.append(wielomian_a[i])

    for i in range(min_dlugosc, len(wielomian_b)):
        wynik.append(wielomian_b[i])

    return wynik


def test_suma_wielomianow():
    assert suma_wielomianow([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
    assert suma_wielomianow([1, 2, 3], [1, 2, 3, 4]) == [2, 4, 6, 4]


if __name__ == "__main__":
    test_suma_wielomianow()
