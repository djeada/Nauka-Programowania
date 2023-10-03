"""
Tytul: Wyszukiwanie liniowe rekurencyjnie.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna klucz. Przy uzyciu rekurencji znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna klucz.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostac zwrocona liczba: 1.

"""


def wyszukiwani_liniowe(lista, klucz):
    """
    Funkcja zwraca indeks klucza w liscie przy pomocy rekurenkcji.
    Jesli klucz nie wystepuje w liscie, zwroc -1.
    """
    if len(lista) == 0:
        return -1

    if lista[0] == klucz:
        return 0

    if wyszukiwani_liniowe(lista[1:], klucz) != -1:
        return 1 + wyszukiwani_liniowe(lista[1:], klucz)

    return -1


def test_wyszukiwani_liniowe():
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 3) == 2
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 6) == -1


if __name__ == "__main__":

    test_wyszukiwani_liniowe()
