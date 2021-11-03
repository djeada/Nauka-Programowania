"""
Otrzymujesz listę n współczynników wielomianu postaci a_nx^n + a_(n-1)x^(n-1) + ... + a_0
oraz liczbę x. Oblicz współczynniki wielomianu będącego wynikiem 
przemnożenia otrzymanego wielomianu przez liczbę x.
"""

def mnozenie_wielomianu(wspolczynniki, x):
    '''
    Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu przez liczbę x.
    '''
    return [wspolczynnik * x for wspolczynnik in wspolczynniki]

def test_mnozenie_wielomianu():
    assert mnozenie_wielomianu([1, 2, 3, 4], 2) == [2, 4, 6, 8]

if __name__ == "__main__":

    test_mnozenie_wielomianu()

