"""
Otrzymujesz listę oraz klucz. Znajdź indeks odpowiadający 
pierwszemu wystąpieniu klucza w liście. Jeśli klucz nie 
wystęþuje w liście, zwróć -1.
"""

def znajdz_klucz(lista, klucz):

    for i in range(len(lista)):
        if lista[i] == klucz:
            return i
    return -1

def test_znajdz_klucz():
    assert znajdz_klucz([1, 2, 3, 4, 5], 5) == 4
    assert znajdz_klucz([1, 2, 3, 4, 5], 6) == -1


if __name__ == "__main__":

    test_znajdz_klucz()
