"""
Tytul: Obliczenie iloczynu wielomianu przez skalar.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe x. Oblicz wspolczynniki wielomianu, ktory jest wynikiem pomnozenia otrzymanego wielomianu przez liczbe x.
Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Lista liczb naturalnych.
Przyklad:
Dla listy wspolczynnikow [4, -3, 2] i liczby x = -2, zostanie zwrocona lista [-8, 6, -4].

"""


def mnozenie_wielomianu(wspolczynniki, x):
    """
    Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu przez liczbe x.
    """
    return [wspolczynnik * x for wspolczynnik in wspolczynniki]


def test_mnozenie_wielomianu():
    assert mnozenie_wielomianu([1, 2, 3, 4], 2) == [2, 4, 6, 8]


if __name__ == "__main__":

    test_mnozenie_wielomianu()

