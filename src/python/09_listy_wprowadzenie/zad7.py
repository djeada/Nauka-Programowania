"""
Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).
Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Para liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).

"""


def srednia_dwoch_najwiekszych(lista):

    if len(lista) < 2:
        return 0.00

    najwieksza = max(lista)
    najwieksza_druga = max(lista[: lista.index(najwieksza)])
    srednia = (najwieksza + najwieksza_druga) / 2
    return srednia


def test_srednia_dwoch_najwiekszych():

    assert srednia_dwoch_najwiekszych([]) == 0.00
    assert srednia_dwoch_najwiekszych([1]) == 0.00
    assert srednia_dwoch_najwiekszych([1, 2]) == 1.50
    assert srednia_dwoch_najwiekszych([3, 5, -7, 4, 9, -11, 2]) == 7.00
    assert (
        srednia_dwoch_najwiekszych([3, -2, 4, 9, -3, -40, 8, 5, -7, 4, 9, -11, 2])
        == 6.5
    )


if __name__ == "__main__":

    test_srednia_dwoch_najwiekszych()

