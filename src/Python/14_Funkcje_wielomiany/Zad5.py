"""
Otrzymujesz listę n współczynników wielomianu postaci anxn+an-1xn-1+...+a0 
oraz liczbę k. Oblicz współczynniki wielomianu będącego k-tą pochodną 
otrzymanego wielomianu.
"""

def pochodna(wielomian, k):
    """
    Funkcja oblicza k-tą pochodną wielomianu.
    """
    wynik = []
    kopia = wielomian[:]

    for i in range(k):
        wynik = []
        n = len(kopia)
        for i in range(n-1):
            wynik.append(kopia[i] * (n - i - 1))
        kopia = wynik[:]

    return wynik

    
def test_pochodna():
    assert pochodna([4, -3, 2], 1) == [8, -3]
    assert pochodna([13, -6, 0, -1, -1], 2) == [156, -36, 0]


if __name__ == "__main__":
    
    test_pochodna()
