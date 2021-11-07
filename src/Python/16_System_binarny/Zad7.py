"""
Otrzymujesz dziesietna reprezentacje liczby naturalnej. 
Zamien miejscami sasiadujace bity w zapisie binarnym 
otrzymanej liczbie. Zwroc dziesietna reprezentacje wyniku.
"""


def zamien_sasiadow(liczba):
    """
    Funkcja zamienia sasiadujace bity w binarnym zapisie liczby.
    """
    parzyste = liczba & 0xAAAAAAAA
    nieparzyste = liczba & 0x55555555

    parzyste >>= 1
    nieparzyste <<= 1

    return parzyste | nieparzyste


def test_zamien_sasiadow():
    assert zamien_sasiadow(9131) == 4951


if __name__ == "__main__":
    test_zamien_sasiadow()
