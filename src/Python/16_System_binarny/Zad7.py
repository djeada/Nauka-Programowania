"""
Zamien miejscami sasiadujace bity.

1010
0101

Maska 0xAAAAAAAA ma wszystkie parzyste bity ustawione
Maska 0x55555555 ma wszystkie nieparzyste bity ustawione

robiac AND zerujemy te ktore nie sa ustawione w pierwotnej liczbie
nastepnie przesuwamy w lewo prawo
dodajemy za pomoca OR
"""


def zamienSasiadow(liczba):
    parzyste = liczba & 0xAAAAAAAA
    nieparzyste = liczba & 0x55555555

    parzyste >>= 1
    nieparzyste <<= 1

    return parzyste | nieparzyste


if __name__ == "__main__":

    liczba = 9131
    wynik = 4951

    assert zamienSasiadow(liczba) == wynik
