"""
Tytul: Usun klucz.
Tresc: Dla otrzymanej listy: liczb calkowitych oraz klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostac zwrocona lista: [6, 2, 1, 27].

"""
from math import pow


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
