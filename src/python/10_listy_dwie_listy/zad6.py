"""
Tytul: Roznica miedzy dwoma listami.
Tresc: Dla otrzymanych dwoch list liczb calkowitych, znajdz elementy, ktore nie sa czescia wspolna obu list.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5, 1].

"""


def czesc_wspolna(lista_a, lista_b):
    return [x for x in lista_a if x in lista_b]


def test_czesc_wspolna():
    assert set(czesc_wspolna([3, 6, 2, 7, 9], [4, 2, 3, 5, 6])) == set([3, 6, 2])
    assert set(czesc_wspolna([1, 2, 3, 4], [2, 3, 4, 5, 6])) == set([2, 3, 4])


if __name__ == "__main__":
    test_czesc_wspolna()

