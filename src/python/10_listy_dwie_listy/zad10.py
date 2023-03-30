"""
Tytul: Polaczenie dwoch list.
Tresc: Dla otrzymanych dwoch list, zwroc liste, ktora powstala poprzez:
a) Dostawienie drugiej listy na koniec pierwszej listy.
b) Wstawienie elementow o indeksach parzystych z drugiej listy na odpowiadajace im indeksy pierwszej listy.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Lista.
Przyklad:
Dla otrzymanych list [1, 2, 3] oraz [4, 5, 6], w podpunkcie a) powinna zostac zwrocona lista: [1, 2, 3, 4, 5, 6].
W podpunkcie b) powinna zostac zwrocona lista: [4, 2, 6, 3].

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

