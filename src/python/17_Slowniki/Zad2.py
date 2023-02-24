"""
Otrzymujesz dwie listy liczb calkowitych. Zbuduj slownik skladajacy sie z 
kluczy bedacych elementami pierwszej listy i wartosciami bedacymi elementami 
drugiej listy. Jesli listy sa roznej dlugosci zwroc pusty slownik.
"""


def stworz_slownik(lista_a, lista_b):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace elementami 
    pierwszej listy i wartosci bedace elementami drugiej listy.
    """

    if len(lista_a) != len(lista_b):
        return {}

    return dict(zip(lista_a, lista_b))


def test_stworz_slownik():
    assert stworz_slownik([1, 2, 3], [4, 5, 6]) == {1: 4, 2: 5, 3: 6}
    assert stworz_slownik([1, 2, 3], [4, 5]) == {}


if __name__ == "__main__":

    test_stworz_slownik()
