"""
Otrzymujesz liczbę N. Przy użyciu rekurencji 
oblicz wartość N-tego wyrazu ciągu Fibonacciego.
"""

def wyraz_ciag_fibonacciego(n):
    """
    Funkcja oblicza n-ty wyraz ciągu Fibonacciego.
    """
    if n < 0:
        raise ValueError("Liczba musi być nieujemna")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return wyraz_ciag_fibonacciego(n-1) + wyraz_ciag_fibonacciego(n-2)


def test_wyraz_ciag_fibonacciego():
    assert wyraz_ciag_fibonacciego(0) == 0
    assert wyraz_ciag_fibonacciego(1) == 1
    assert wyraz_ciag_fibonacciego(12) == 144

if __name__ == "__main__":
    
    test_wyraz_ciag_fibonacciego()