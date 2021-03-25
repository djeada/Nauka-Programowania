"""
Ile bitow nalezy odwrocic by zmienic A w B?
"""


def bityDoZmianyV1(liczbaA, liczbaB):

    n = liczbaA ^ liczbaB

    licznikJedynek = 0
    while n:
        n &= n - 1
        licznikJedynek += 1

    return licznikJedynek


if __name__ == "__main__":

    liczbaA = 34
    liczbaB = 73
    wynik = 5

    assert bityDoZmianyV1(liczbaA, liczbaB) == wynik
