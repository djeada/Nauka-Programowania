"""
Ile bitow nalezy odwrocic by zmienic A w B?
"""


def bity_do_zmiany_v1(liczba_a, liczba_b):

    n = liczba_a ^ liczba_b

    licznik_jedynek = 0
    while n:
        n &= n - 1
        licznik_jedynek += 1

    return licznik_jedynek


if __name__ == "__main__":

    liczba_a = 34
    liczba_b = 73
    wynik = 5

    assert bity_do_zmiany_v1(liczba_a, liczba_b) == wynik
