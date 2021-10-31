from math import pow

"""
Dla otrzymanej listy oraz klucza, usun pierwsze 
wystapienie klucza w liscie.
"""


def usun_klucz(lista, klucz):
    for i in range(len(lista)):
        if lista[i] == klucz:
            lista.pop(i)
            return lista
    return lista


def test_usun_klucz():
    assert usun_klucz([1, 2, 3, 3], 3) == [1, 2, 3]
    assert usun_klucz([1, 2, 3, 3], 4) == [1, 2, 3, 3]
    assert usun_klucz([1, 1, 1, 1], 1) == [1, 1, 1]


if __name__ == "__main__":

    test_usun_klucz()
