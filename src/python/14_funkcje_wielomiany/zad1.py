"""
Tytul: Obliczenie wartosci wielomianu w punkcie.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna x. Znajdz wartosc wielomianu w podanym punkcie.
Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla listy wspolczynnikow [3, 2, 1] i liczby x = 1, zostanie zwrocona liczba 6.

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

