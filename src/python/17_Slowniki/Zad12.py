"""
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. 
Listy sa nieuporzadkowane. Sprawdz czy slowniki skladaja sie z tych samych par. 
Dwie listy uznajemy za identyczne jesli zawieraja te same elementy, przy 
czym kolejnosc elementow moze byc zmieniona.
"""


def czy_slowniki_identyczne(slownik_a, slownik_b):
    """
    Funkcja sprawdza czy dwa slowniki maja takie same elementy.
    """
    for klucz in slownik_a:
        if klucz not in slownik_b:
            return False
        elif sorted(slownik_a[klucz]) != sorted(slownik_b[klucz]):
            return False
    return True


def test_czy_slowniki_identyczne():

    assert czy_slowniki_identyczne(
        {"a": [1, 2, 3], "b": [4, 5, 6]}, {"a": [3, 1, 2], "b": [5, 4, 6]}
    )


if __name__ == "__main__":

    test_czy_slowniki_identyczne()
