"""
Sprawdz czy slowo jest palindromem. Palindrom to slowo brzmiace tak samo 
czytane od lewej do prawej i od prawej do lewej.
"""


def czy_palindrom(napis):
    """
    Funkcja sprawdza czy podany napis jest palindromem.
    """
    return napis == napis[::-1]


def test_czy_palindrom():
    assert czy_palindrom("kajak")
    assert not czy_palindrom("Pan")


if __name__ == "__main__":
    test_czy_palindrom()
