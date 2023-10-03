"""
Tytul: Slownik z kluczami bedacymi liczbami naturalnymi i wartosciami ich kwadratami.
Tresc: Dostajesz liczbe naturalna. Stworz slownik, w ktorym kluczami beda kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartosciami beda ich kwadraty.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami naturalnymi.
Przyklad:
Dla liczby 5, slownik powinien wygladac nastepujaco: {1: 1, 2: 4, 3: 9, 4: 16}.

"""


def stworz_slownik(n):
    """
    Funkcja tworzy slownik zawierajacy klucze bedace kolejnymi
    liczbami naturalnymi mniejszymi od podanej liczby n
    oraz wartosci bedacymi kwadratami kluczy.
    """

    slownik = {}
    for i in range(n):
        slownik[i] = i ** 2
    return slownik


def test_stworz_slownik():
    assert stworz_slownik(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    assert stworz_slownik(0) == {}


if __name__ == "__main__":

    test_stworz_slownik()
