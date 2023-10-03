"""
Tytul: Znalezienie brakujacego elementu w liscie.
Tresc: Dla dostarczonej listy, skladajacej sie z nieuporzadkowanych kolejnych (oprocz jednego) elementow ciagu arytmetycznego, znajdz brakujacy element.
Dane wejsciowe: Lista zawierajaca liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrocona liczba: 4.

"""


def suma_ciag_aryt(lista):
    return (len(lista) + 1) * (min(lista) + max(lista)) // 2


def brakujacy_element(lista):

    suma_przedzialu = suma_ciag_aryt(lista)
    suma_listy = sum(lista)

    wynik = suma_przedzialu - suma_listy

    if wynik not in lista:
        return wynik

    return 0


def test_brakujacy_element():
    assert brakujacy_element([6, 8, 4, 10, 14, 2]) == 12
    assert brakujacy_element([1, 2, 4, 5, 6]) == 3
    assert brakujacy_element([1, 2, 3]) == 0


if __name__ == "__main__":

    test_brakujacy_element()
