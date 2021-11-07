"""
Otrzymujesz liczbe N. Przy uzyciu rekurencji 
oblicz silnie z otrzymanej liczby.
"""


def silnia(n):
    """
    Funkcja oblicza silnie z n.
    """
    if n < 0:
        raise ValueError("Silnia jest niezdefiniowana dla liczb ujemnych.")

    if n <= 1:
        return 1

    return n * silnia(n - 1)


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(5) == 120
    assert silnia(10) == 3628800


if __name__ == "__main__":
    test_silnia()
