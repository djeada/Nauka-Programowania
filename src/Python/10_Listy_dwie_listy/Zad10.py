"""
Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci. 
Znajdz ich mediane.
"""


def mediana_list(lista_a, list_b):
    lista_a.extend(list_b)
    lista_a.sort()
    return lista_a[len(lista_a) // 2]


def test_mediana_list():
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 7
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]) == 8


if __name__ == "__main__":

    test_mediana_list()
