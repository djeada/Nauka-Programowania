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


def dostawienie_na_koniec(lista_a, lista_b):
    lista_a.extend(lista_b)
    return lista_a


def wstawianie_parzystych_indeksow(lista_a, lista_b):
    for i in range(len(lista_a)):
        if i % 2 == 0:
            del lista_a[i]
            lista_a.insert(i, lista_b[i])
    return lista_a


def test_dostawienie_na_koniec():
    assert dostawienie_na_koniec([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_wstawianie_parzystych_indeksow():
    assert wstawianie_parzystych_indeksow([1, 1, 1], [4, 5, 6]) == [4, 1, 6]


if __name__ == "__main__":

    test_dostawienie_na_koniec()
    test_wstawianie_parzystych_indeksow()
