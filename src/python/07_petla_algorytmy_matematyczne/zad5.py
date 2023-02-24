"""
Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci 
ich najwiekszy wspolny dzielnik.
"""


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def test_nwd():
    assert nwd(12, 15) == 3
    assert nwd(15, 12) == 3
    assert nwd(9, 6) == 3
    assert nwd(6, 9) == 3


if __name__ == "__main__":
    test_nwd()
