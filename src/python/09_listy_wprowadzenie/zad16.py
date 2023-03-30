"""
Tytul: Usun klucz.
Tresc: Dla otrzymanej listy: liczb calkowitych oraz klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostac zwrocona lista: [6, 2, 1, 27].

"""


def znajdz_pare(lista, x):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                return i, j
    return -1, -1


def test_znajdz_pare():
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == (0, 8)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22) == (-1, -1)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == (0, 6)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == (-1, -1)


if __name__ == "__main__":

    test_znajdz_pare()

