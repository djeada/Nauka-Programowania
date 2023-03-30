"""
Tytul: Sprawdzanie czy macierz jest "magiczna".
Tresc: Otrzymujesz macierz kwadratowa. Sprawdz, czy jest ona kwadratem magicznym.
Podpowiedz: Kwadrat magiczny sklada sie z powtarzajacych sie dodatnich liczb naturalnych. Suma elementow w kazdym wierszu, w kazdej kolumnie oraz na kazdej przekatnej jest taka sama.
Dane wejsciowe: Lista list liczb naturalnych.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanej macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostac zwrocona wartosc logiczna: Prawda.

"""
import string


def polacz_listy_w_macierz(lista_a, lista_b):
    """
    Funkcja zwraca macierz dwuwymiarowa, ktorej pierwsza kolumna sklada sie z
    elementow pierwszej listy, a druga kolumna elementow drugiej listy.
    Jesli otrzymane listy nie sa rownej dlugosci zwroc pusta macierz.
    """
    if len(lista_a) != len(lista_b):
        return []
    macierz = []
    for element_a, element_b in zip(lista_a, lista_b):
        macierz.append(element_a, element_b)
    return macierz


def test_polacz_listy_w_macierz():
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5]) == []


if __name__ == "__main__":
    test_polacz_listy_w_macierz()

