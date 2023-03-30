"""
Tytul: Usun z pierwszej listy czesc wspolna obu list.
Tresc: Otrzymujesz dwie listy liczb calkowitych. Usun z pierwszej listy te elementy, ktore wystepuja rowniez w drugiej liscie.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5].

"""


def polacz_posortowane_listy(lista_a, lista_b):
    lista_c = []
    while lista_a and lista_b:
        if lista_a[0] < lista_b[0]:
            lista_c.append(lista_a.pop(0))
        else:
            lista_c.append(lista_b.pop(0))
    lista_c.extend(lista_a)
    lista_c.extend(lista_b)
    return lista_c


def test_polacz_posortowane_listy():
    assert polacz_posortowane_listy([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert polacz_posortowane_listy([1, 3, 5], []) == [1, 3, 5]
    assert polacz_posortowane_listy([], [1, 3, 5]) == [1, 3, 5]
    assert polacz_posortowane_listy([], []) == []


if __name__ == "__main__":

    test_polacz_posortowane_listy()

