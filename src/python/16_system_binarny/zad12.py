"""
Otrzymujesz dziesietna reprezentacje liczby naturalnej. 
Oblicz dlugosc najdluzszego ciagu zer w jej binarnej reprezentacji.
"""


def najdluzszy_ciag_zer(liczba):
    """
    Funkcja zwraca dlugosc najdluzszego ciagu zer w dziesietnej
    reprezentacji liczby binarnej.
    """
    liczba_bin = bin(liczba)
    liczba_bin = liczba_bin[2:]
    liczba_bin = liczba_bin.split("1")
    liczba_bin.sort(key=len)
    return len(liczba_bin[-1])


def test_najdluzszy_ciag_zer():
    assert najdluzszy_ciag_zer(0) == 1
    assert najdluzszy_ciag_zer(111) == 1
    assert najdluzszy_ciag_zer(8219) == 8


if __name__ == "__main__":

    test_najdluzszy_ciag_zer()
