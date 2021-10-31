"""
Otrzymujesz dwie listy liczb całkowitych. Usuń z pierwszej 
listy te elementy, które występują również w drugiej liście.
"""


def usun_czesc_wspolna(lista_a, lista_b):
    for element in lista_a:
        if element in lista_b:
            lista_a.remove(element)
    return lista_a


def test_usun_czesc_wspolna():
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == []
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == [5]
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7]) == [5, 6, 7]


if __name__ == "__main__":

    test_usun_czesc_wspolna()
