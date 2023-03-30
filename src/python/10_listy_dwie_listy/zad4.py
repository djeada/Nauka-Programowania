"""
Tytul: Obliczenie sredniej wazonej.
Tresc: Otrzymujesz dwie listy liczb zmiennoprzecinkowych. Pierwsza lista reprezentuje wagi, a druga wartosci. Oblicz srednia wazona.
Dane wejsciowe: Dwie listy liczb zmiennoprzecinkowych.
Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2.0, 5.0, 0.0, 2.0, 1.0] oraz [0.2, 0.4, 0.1, 0.2, 0.1] zostanie zwrocona wartosc: 0.29.

"""


def iloczyn_wektorowy(lista_a, lista_b):

    if len(lista_a) != len(lista_b):
        print(
            "Nie mozna obliczyc iloczynu wektorowego, poniewaz listy nie maja takiej samej dlugosci"
        )
        return
    if len(lista_a) != 3:
        print(
            "Nie mozna obliczyc iloczynu wektorowego, poniewaz listy nie sa 3-wymiarowe"
        )
        return

    wynik = (
        lista_a[1] * lista_b[2] - lista_a[2] * lista_b[1],
        lista_a[2] * lista_b[0] - lista_a[0] * lista_b[2],
        lista_a[0] * lista_b[1] - lista_a[1] * lista_b[0],
    )
    return list(wynik)


def test_iloczyn_wektorowy():

    assert iloczyn_wektorowy([1, 2, 3], [4, 5, 6]) == [-3, 6, -3]
    assert iloczyn_wektorowy([0, -5, 8], [3, 7, -2]) == [-46, 24, 15]


if __name__ == "__main__":

    test_iloczyn_wektorowy()

