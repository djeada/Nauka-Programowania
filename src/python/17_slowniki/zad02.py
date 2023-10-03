"""
Tytul: Slownik z kluczami bedacymi elementami jednej listy i wartosciami elementami drugiej listy.
Tresc: Dostajesz dwie listy liczb calkowitych. Stworz slownik, w ktorym kluczami beda elementy pierwszej listy, a wartosciami elementy drugiej listy. Jesli listy sa roznej dlugosci, zwroc pusty slownik.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami calkowitymi.
Przyklad:
Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], slownik powinien wygladac nastepujaco: {3: 1, 5: 2, 8: -1}.

"""


def stworz_slownik(lista_a, lista_b):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace elementami
    pierwszej listy i wartosci bedace elementami drugiej listy.
    """

    if len(lista_a) != len(lista_b):
        return {}

    return dict(zip(lista_a, lista_b))


def test_stworz_slownik():
    assert stworz_slownik([1, 2, 3], [4, 5, 6]) == {1: 4, 2: 5, 3: 6}
    assert stworz_slownik([1, 2, 3], [4, 5]) == {}


if __name__ == "__main__":

    test_stworz_slownik()
