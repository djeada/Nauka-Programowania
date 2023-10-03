"""
Tytul: Usun z pierwszej listy czesc wspolna obu list.
Tresc: Otrzymujesz dwie listy liczb calkowitych. Usun z pierwszej listy te elementy, ktore wystepuja rowniez w drugiej liscie.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5].

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
