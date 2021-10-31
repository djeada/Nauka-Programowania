"""
Otrzymujesz dwie listy liczb calkowitych. Znajdz elementy, 
ktore nie sa czescia wspolna obu list.
"""


def roznica_list(lista_a, lista_b):
    return [x for x in lista_a if x not in lista_b] + [
        x for x in lista_b if x not in lista_a
    ]


def test_roznica_list():
    assert set(roznica_list([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])) == set([1, 6])
    assert set(roznica_list([9, 4, -2, -1], [9, 4, -2, -1])) == set()
    assert set(roznica_list([2, 5, 9], [3, 5, 1])) == set([2, 9, 3, 1])


if __name__ == "__main__":

    test_roznica_list()
