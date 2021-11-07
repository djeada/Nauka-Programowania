"""
Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie 
z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi 
od otrzymanej liczby oraz wartosci bedacych kwadratami 
odpowiadajacych im kluczy.
"""


def stworz_slownik(n):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace kolejnymi 
    liczbami naturalnymi mniejszymi od podanej liczby n 
    oraz wartosci bedacymi kwadratami kluczy.
    """

    slownik = {}
    for i in range(n):
        slownik[i] = i ** 2
    return slownik


def test_stworz_slownik():
    assert stworz_slownik(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    assert stworz_slownik(0) == {}


if __name__ == "__main__":

    test_stworz_slownik()
