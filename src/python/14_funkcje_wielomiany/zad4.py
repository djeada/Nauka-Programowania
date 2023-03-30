"""
Tytul: Mnozenie wielomianow.
Tresc: Otrzymujesz dwie listy n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$. Oblicz wspolczynniki wielomianu bedacego iloczynem otrzymanych wielomianow.
Dane wejsciowe: Dwie listy liczb naturalnych.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla otrzymanych dwoch list: [5, 0, 10, 6] oraz [1, 2, 4], zostanie zwrocona lista: [5, 10, 30, 26, 52, 24].

"""


def iloczyn_wielomianow(wielomian_a, wielomian_b):
    """
    Funkcja zwraca wspolczynniki wielomianu bedacego iloczynem wielomianow a i b.
    """

    wynik = [0 for i in range(len(wielomian_a) + len(wielomian_b) - 1)]

    for i in range(len(wielomian_a)):
        for j in range(len(wielomian_b)):
            wynik[i + j] += wielomian_a[i] * wielomian_b[j]

    return wynik


def test_iloczyn_wielomianow():
    assert iloczyn_wielomianow([1, 1, 0], [-5, 0, 0, 2]) == [-5, -5, 0, 2, 2, 0]


if __name__ == "__main__":
    test_iloczyn_wielomianow()

