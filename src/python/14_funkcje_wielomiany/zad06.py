"""
Tytul: Obliczenie miejsc zerowych rownania kwadratowego.
Tresc: Otrzymujesz liste wspolczynnikow rownania kwadratowego $ax^2 + bx + c$. Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Lista liczb zmiennoprzecinkowych.
Przyklad:
Dla otrzymanej listy wspolczynnikow: [1, 2, 1], zostanie zwrocona lista: [-1, -1].

"""


def miesca_zerowe(wspolczynniki):
    """
    Funkcja zwraca liste miejsc zerowych rownania kwadratowego.
    """
    a = wspolczynniki[0]
    b = wspolczynniki[1]
    c = wspolczynniki[2]
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return [-b / (2 * a) + delta ** 0.5, -b / (2 * a) - delta ** 0.5]


def test_miesca_zerowe():

    assert miesca_zerowe([1, 2, 1]) == [-1]
    assert miesca_zerowe([3, 9, -12]) == [13.5, -16.5]


if __name__ == "__main__":

    test_miesca_zerowe()
